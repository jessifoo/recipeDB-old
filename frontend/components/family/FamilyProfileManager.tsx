import type React from 'react';
import { useState } from 'react';

import {
  Box,
  Button,
  FormControl,
  FormLabel,
  Heading,
  Input,
  Tag,
  TagCloseButton,
  TagLabel,
  Text,
  VStack,
  Wrap,
  WrapItem,
  useToast,
} from '@chakra-ui/react';

import { useFamilyProfile } from '@/stores/familyProfileStore';

export function FamilyProfileManager() {
  const toast = useToast();
  const { members, addMember, updateMember } = useFamilyProfile();
  const [newAllergy, setNewAllergy] = useState('');
  const [newTrigger, setNewTrigger] = useState('');
  const [name, setName] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name) {
      toast({
        title: 'Name required',
        status: 'error',
        duration: 2000,
      });
      return;
    }

    addMember({
      name,
      allergies: [],
      fpiesTriggers: [],
      safeSubstitutes: {},
    });

    setName('');
    toast({
      title: 'Family member added',
      status: 'success',
      duration: 2000,
    });
  };

  const addAllergy = (memberId: string) => {
    if (!newAllergy) {
      return;
    }
    const member = members.find((m) => m.id === memberId);
    if (member && !member.allergies.includes(newAllergy)) {
      updateMember(memberId, {
        allergies: [...member.allergies, newAllergy],
      });
      setNewAllergy('');
    }
  };

  const addTrigger = (memberId: string) => {
    if (!newTrigger) {
      return;
    }
    const member = members.find((m) => m.id === memberId);
    if (member && !member.fpiesTriggers.includes(newTrigger)) {
      updateMember(memberId, {
        fpiesTriggers: [...member.fpiesTriggers, newTrigger],
      });
      setNewTrigger('');
    }
  };

  const removeAllergy = (memberId: string, allergy: string) => {
    const member = members.find((m) => m.id === memberId);
    if (member) {
      updateMember(memberId, {
        allergies: member.allergies.filter((a) => a !== allergy),
      });
    }
  };

  const removeTrigger = (memberId: string, trigger: string) => {
    const member = members.find((m) => m.id === memberId);
    if (member) {
      updateMember(memberId, {
        fpiesTriggers: member.fpiesTriggers.filter((t) => t !== trigger),
      });
    }
  };

  return (
    <Box p={6}>
      <VStack spacing={8} align="stretch">
        <Box>
          <Heading size="md" mb={4}>
            Add Family Member
          </Heading>
          <form onSubmit={handleSubmit}>
            <FormControl>
              <FormLabel>Name</FormLabel>
              <Input
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Enter name"
                mb={4}
              />
              <Button type="submit" colorScheme="blue">
                Add Family Member
              </Button>
            </FormControl>
          </form>
        </Box>

        {members.map((member) => (
          <Box key={member.id} p={4} borderWidth={1} borderRadius="md">
            <Heading size="md" mb={4}>
              {member.name}'s Profile
            </Heading>

            <VStack align="stretch" spacing={4}>
              {/* Allergies Section */}
              <Box>
                <Text fontWeight="bold" mb={2}>
                  Allergies
                </Text>
                <Wrap mb={2}>
                  {member.allergies.map((allergy) => (
                    <WrapItem key={allergy}>
                      <Tag size="md" colorScheme="red" borderRadius="full">
                        <TagLabel>{allergy}</TagLabel>
                        <TagCloseButton
                          onClick={() => removeAllergy(member.id, allergy)}
                        />
                      </Tag>
                    </WrapItem>
                  ))}
                </Wrap>
                <FormControl display="flex">
                  <Input
                    value={newAllergy}
                    onChange={(e) => setNewAllergy(e.target.value)}
                    placeholder="Add allergy"
                    size="sm"
                    mr={2}
                  />
                  <Button
                    size="sm"
                    onClick={() => addAllergy(member.id)}
                    colorScheme="blue"
                  >
                    Add
                  </Button>
                </FormControl>
              </Box>

              {/* FPIES Triggers Section */}
              <Box>
                <Text fontWeight="bold" mb={2}>
                  FPIES Triggers
                </Text>
                <Wrap mb={2}>
                  {member.fpiesTriggers.map((trigger) => (
                    <WrapItem key={trigger}>
                      <Tag size="md" colorScheme="orange" borderRadius="full">
                        <TagLabel>{trigger}</TagLabel>
                        <TagCloseButton
                          onClick={() => removeTrigger(member.id, trigger)}
                        />
                      </Tag>
                    </WrapItem>
                  ))}
                </Wrap>
                <FormControl display="flex">
                  <Input
                    value={newTrigger}
                    onChange={(e) => setNewTrigger(e.target.value)}
                    placeholder="Add FPIES trigger"
                    size="sm"
                    mr={2}
                  />
                  <Button
                    size="sm"
                    onClick={() => addTrigger(member.id)}
                    colorScheme="blue"
                  >
                    Add
                  </Button>
                </FormControl>
              </Box>
            </VStack>
          </Box>
        ))}
      </VStack>
    </Box>
  );
}
