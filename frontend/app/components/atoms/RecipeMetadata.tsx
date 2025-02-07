import { HStack, Icon, Text } from '@chakra-ui/react';
import { IconType } from 'react-icons';
import { FaClock, FaGlobe, FaUtensils } from 'react-icons/fa';

interface MetadataItemProps {
  icon: IconType;
  label: string;
}

function MetadataItem({ icon, label }: MetadataItemProps) {
  return (
    <HStack spacing={1} color="gray.600">
      <Icon as={icon} fontSize="sm" />
      <Text fontSize="sm" fontWeight="medium">
        {label}
      </Text>
    </HStack>
  );
}

interface RecipeMetadataProps {
  cookingTime?: number;
  servings?: number;
  cuisine?: string;
}

export function RecipeMetadata({
  cookingTime,
  servings,
  cuisine,
}: RecipeMetadataProps) {
  return (
    <HStack spacing={4} mt={2}>
      {cookingTime && (
        <MetadataItem icon={FaClock} label={`${cookingTime} min`} />
      )}
      {servings && (
        <MetadataItem icon={FaUtensils} label={`${servings} servings`} />
      )}
      {cuisine && <MetadataItem icon={FaGlobe} label={cuisine} />}
    </HStack>
  );
}
