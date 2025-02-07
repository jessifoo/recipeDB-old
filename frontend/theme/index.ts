import { extendTheme } from '@chakra-ui/react';

const components = {
  Container: {
    baseStyle: {
      maxW: 'container.xl',
      px: { base: 4, md: 8 },
      py: 8,
    },
  },
  Card: {
    baseStyle: {
      container: {
        borderWidth: '1px',
        borderRadius: 'lg',
        overflow: 'hidden',
        bg: 'white',
        _dark: {
          bg: 'gray.800',
        },
        transition: 'all 0.2s',
        _hover: { shadow: 'md' },
      },
      body: {
        p: 6,
      },
      image: {
        height: '200px',
        width: '100%',
        objectFit: 'cover',
      },
    },
  },
  Heading: {
    baseStyle: {
      mb: 4,
    },
    variants: {
      pageTitle: {
        fontSize: '2xl',
        fontWeight: 'bold',
        mb: 8,
      },
      sectionTitle: {
        fontSize: 'xl',
        fontWeight: 'semibold',
        mb: 4,
      },
    },
  },
  Text: {
    variants: {
      secondary: {
        color: 'gray.600',
        _dark: {
          color: 'gray.400',
        },
      },
      error: {
        color: 'red.500',
      },
      empty: {
        color: 'gray.500',
        textAlign: 'center',
      },
    },
  },
  Button: {
    variants: {
      filter: {
        variant: 'ghost',
        size: 'sm',
      },
    },
  },
  Grid: {
    variants: {
      responsive: {
        templateColumns: {
          base: '1fr',
          md: 'repeat(2, 1fr)',
          lg: 'repeat(3, 1fr)',
        },
        gap: 6,
      },
      filters: {
        templateColumns: {
          base: '1fr',
          md: 'repeat(3, 1fr)',
        },
        gap: 4,
      },
    },
  },
  Form: {
    baseStyle: {
      container: {
        p: 4,
        borderWidth: '1px',
        borderRadius: 'lg',
        bg: 'white',
        _dark: {
          bg: 'gray.800',
        },
        shadow: 'sm',
      },
    },
  },
};

const theme = extendTheme({
  components,
  styles: {
    global: {
      body: {
        bg: 'gray.50',
        _dark: {
          bg: 'gray.900',
        },
      },
    },
  },
});

export default theme;
