import {
  Box,
  Container,
  Grid,
  Heading,
  Link,
  useColorModeValue,
} from '@chakra-ui/react';
import { useRouter } from 'next/router';
import { MDXRemote } from 'next-mdx-remote';
import { serialize } from 'next-mdx-remote/serialize';
import fs from 'node:fs';
import path from 'node:path';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { tomorrow } from 'react-syntax-highlighter/dist/cjs/styles/prism';

import type { GetStaticPaths, GetStaticProps } from 'next';

interface DocsPageProps {
  source: string;
  components: { name: string; path: string }[];
}

const _components = {
  code: ({ children, className }) => {
    const language = className
      ? className.replace('language-', '')
      : 'typescript';
    return (
      <SyntaxHighlighter
        language={language}
        style={tomorrow}
        customStyle={{
          margin: '1.5rem 0',
          borderRadius: '0.5rem',
        }}
      >
        {children}
      </SyntaxHighlighter>
    );
  },
  // Add other MDX components here
};

export default function DocsPage({ source, components }: DocsPageProps) {
  const router = useRouter();
  const bgColor = useColorModeValue('white', 'gray.800');
  const borderColor = useColorModeValue('gray.200', 'gray.700');

  return (
    <Container maxW="container.xl" py={8}>
      <Grid templateColumns={{ base: '1fr', md: '250px 1fr' }} gap={8}>
        {/* Sidebar */}
        <Box
          position="sticky"
          top="4"
          height="fit-content"
          p={4}
          bg={bgColor}
          borderRadius="md"
          borderWidth="1px"
          borderColor={borderColor}
        >
          <Heading size="md" mb={4}>
            Components
          </Heading>
          {components.map(({ name, path }) => (
            <Link
              key={path}
              display="block"
              py={2}
              color={router.query.slug?.[0] === path ? 'accent.500' : undefined}
              onClick={() => router.push(`/docs/${path}`)}
              cursor="pointer"
              _hover={{ color: 'accent.500' }}
            >
              {name}
            </Link>
          ))}
        </Box>

        {/* Content */}
        <Box
          p={6}
          bg={bgColor}
          borderRadius="md"
          borderWidth="1px"
          borderColor={borderColor}
        >
          <MDXRemote {...source} components={_components} />
        </Box>
      </Grid>
    </Container>
  );
}

export const getStaticPaths: GetStaticPaths = async () => {
  const docsDir = path.join(process.cwd(), 'public/docs/components');
  const files = fs.readdirSync(docsDir);

  const paths = files.map((file) => ({
    params: { slug: [file.replace('.md', '')] },
  }));

  return {
    paths: [
      { params: { slug: [] } }, // Root docs page
      ...paths,
    ],
    fallback: false,
  };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const docsDir = path.join(process.cwd(), 'public/docs/components');
  let content = '';

  if (params?.slug?.[0]) {
    const filePath = path.join(docsDir, `${params.slug[0]}.md`);
    content = fs.readFileSync(filePath, 'utf8');
  } else {
    content =
      '# Documentation\n\nSelect a component from the sidebar to view its documentation.';
  }

  const mdxSource = await serialize(content);

  // Get list of all component docs
  const files = fs.readdirSync(docsDir);
  const components = files.map((file) => ({
    name: file.replace('.md', ''),
    path: file.replace('.md', ''),
  }));

  return {
    props: {
      source: mdxSource,
      components,
    },
  };
};
