def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.9867, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5886, "metric_value": 0.954, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Passanger", "instances": 5298, "metric_value": 0.9388, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 3502, "metric_value": 0.9635, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Occupation", "instances": 2300, "metric_value": 0.9739, "depth": 5}
					if obj[3]>0:
						# {"feature": "Education", "instances": 2269, "metric_value": 0.9757, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Direction_same", "instances": 2105, "metric_value": 0.9784, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 1326, "metric_value": 0.9845, "depth": 8}
								if obj[4]<=3.0:
									return 'True'
								elif obj[4]>3.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 779, "metric_value": 0.9658, "depth": 8}
								if obj[4]>-1.0:
									return 'True'
								elif obj[4]<=-1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Direction_same", "instances": 164, "metric_value": 0.9262, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 98, "metric_value": 0.8631, "depth": 8}
								if obj[4]>-1.0:
									return 'True'
								elif obj[4]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 66, "metric_value": 0.9834, "depth": 8}
								if obj[4]<=0.0:
									return 'True'
								elif obj[4]>0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Education", "instances": 31, "metric_value": 0.6374, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Direction_same", "instances": 23, "metric_value": 0.5586, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 16, "metric_value": 0.5436, "depth": 8}
								if obj[4]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 8}
								if obj[4]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>0:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[4]<=2.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Education", "instances": 1202, "metric_value": 0.9387, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 746, "metric_value": 0.9657, "depth": 6}
						if obj[3]<=16:
							# {"feature": "Direction_same", "instances": 685, "metric_value": 0.9726, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 437, "metric_value": 0.9868, "depth": 8}
								if obj[4]<=3.0:
									return 'True'
								elif obj[4]>3.0:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 248, "metric_value": 0.9348, "depth": 8}
								if obj[4]>0.0:
									return 'True'
								elif obj[4]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>16:
							# {"feature": "Bar", "instances": 61, "metric_value": 0.8302, "depth": 7}
							if obj[4]>0.0:
								# {"feature": "Direction_same", "instances": 54, "metric_value": 0.8767, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 456, "metric_value": 0.8764, "depth": 6}
						if obj[3]<=18:
							# {"feature": "Direction_same", "instances": 418, "metric_value": 0.8888, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Bar", "instances": 275, "metric_value": 0.8699, "depth": 8}
								if obj[4]>0.0:
									return 'True'
								elif obj[4]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Bar", "instances": 143, "metric_value": 0.9206, "depth": 8}
								if obj[4]<=3.0:
									return 'True'
								elif obj[4]>3.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[3]>18:
							# {"feature": "Bar", "instances": 38, "metric_value": 0.6892, "depth": 7}
							if obj[4]<=2.0:
								# {"feature": "Direction_same", "instances": 31, "metric_value": 0.5548, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>2.0:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Bar", "instances": 1796, "metric_value": 0.871, "depth": 4}
				if obj[4]<=3.0:
					# {"feature": "Occupation", "instances": 1728, "metric_value": 0.8641, "depth": 5}
					if obj[3]<=13.254023638937538:
						# {"feature": "Restaurant20to50", "instances": 1490, "metric_value": 0.8772, "depth": 6}
						if obj[5]<=1.0:
							# {"feature": "Education", "instances": 1022, "metric_value": 0.8989, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Direction_same", "instances": 947, "metric_value": 0.9043, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Direction_same", "instances": 75, "metric_value": 0.8165, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>1.0:
							# {"feature": "Education", "instances": 468, "metric_value": 0.8213, "depth": 7}
							if obj[2]>1:
								# {"feature": "Direction_same", "instances": 291, "metric_value": 0.8625, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=1:
								# {"feature": "Direction_same", "instances": 177, "metric_value": 0.7396, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>13.254023638937538:
						# {"feature": "Restaurant20to50", "instances": 238, "metric_value": 0.765, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Education", "instances": 221, "metric_value": 0.7947, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 156, "metric_value": 0.8494, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 65, "metric_value": 0.6194, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>3.0:
					# {"feature": "Occupation", "instances": 68, "metric_value": 0.9843, "depth": 5}
					if obj[3]<=12:
						# {"feature": "Education", "instances": 47, "metric_value": 0.9252, "depth": 6}
						if obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9597, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 31, "metric_value": 0.9812, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>12:
						# {"feature": "Education", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[2]<=0:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]>2.0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]>2:
			# {"feature": "Passanger", "instances": 588, "metric_value": 0.9939, "depth": 3}
			if obj[0]>0:
				# {"feature": "Bar", "instances": 570, "metric_value": 0.9897, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 323, "metric_value": 0.9668, "depth": 5}
					if obj[2]<=4:
						# {"feature": "Restaurant20to50", "instances": 322, "metric_value": 0.9656, "depth": 6}
						if obj[5]<=3.0:
							# {"feature": "Occupation", "instances": 312, "metric_value": 0.9694, "depth": 7}
							if obj[3]<=7.842948717948718:
								# {"feature": "Direction_same", "instances": 196, "metric_value": 0.983, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]>7.842948717948718:
								# {"feature": "Direction_same", "instances": 116, "metric_value": 0.9371, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>3.0:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=14:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]>14:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[2]>4:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Education", "instances": 247, "metric_value": 1.0, "depth": 5}
					if obj[2]<=4:
						# {"feature": "Restaurant20to50", "instances": 245, "metric_value": 1.0, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Occupation", "instances": 244, "metric_value": 1.0, "depth": 7}
							if obj[3]>1.4453042020270468:
								# {"feature": "Direction_same", "instances": 195, "metric_value": 0.9995, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]<=1.4453042020270468:
								# {"feature": "Direction_same", "instances": 49, "metric_value": 0.9925, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>4:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Bar", "instances": 18, "metric_value": 0.5033, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[3]<=9:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					elif obj[3]>9:
						return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Bar", "instances": 2261, "metric_value": 0.9801, "depth": 2}
		if obj[4]>0.0:
			# {"feature": "Passanger", "instances": 1286, "metric_value": 0.998, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Restaurant20to50", "instances": 1095, "metric_value": 1.0, "depth": 4}
				if obj[5]<=1.0:
					# {"feature": "Education", "instances": 660, "metric_value": 0.9914, "depth": 5}
					if obj[2]>0:
						# {"feature": "Occupation", "instances": 428, "metric_value": 0.972, "depth": 6}
						if obj[3]<=14.061858607657157:
							# {"feature": "Direction_same", "instances": 363, "metric_value": 0.9857, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 270, "metric_value": 0.9771, "depth": 8}
								if obj[7]<=2:
									return 'False'
								elif obj[7]>2:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 93, "metric_value": 0.9992, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>14.061858607657157:
							# {"feature": "Direction_same", "instances": 65, "metric_value": 0.8051, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 56, "metric_value": 0.7817, "depth": 8}
								if obj[7]>1:
									return 'False'
								elif obj[7]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=1:
									return 'False'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						# {"feature": "Direction_same", "instances": 232, "metric_value": 0.9981, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Occupation", "instances": 178, "metric_value": 0.9999, "depth": 7}
							if obj[3]>5:
								# {"feature": "Distance", "instances": 124, "metric_value": 0.9932, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'True'
								else: return 'True'
							elif obj[3]<=5:
								# {"feature": "Distance", "instances": 54, "metric_value": 0.9751, "depth": 8}
								if obj[7]<=2:
									return 'False'
								elif obj[7]>2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>0:
							# {"feature": "Occupation", "instances": 54, "metric_value": 0.9751, "depth": 7}
							if obj[3]<=22:
								# {"feature": "Distance", "instances": 52, "metric_value": 0.9612, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							elif obj[3]>22:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[5]>1.0:
					# {"feature": "Occupation", "instances": 435, "metric_value": 0.9828, "depth": 5}
					if obj[3]>0:
						# {"feature": "Direction_same", "instances": 430, "metric_value": 0.985, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Education", "instances": 338, "metric_value": 0.9943, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Distance", "instances": 310, "metric_value": 0.9964, "depth": 8}
								if obj[7]>1:
									return 'True'
								elif obj[7]<=1:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								# {"feature": "Distance", "instances": 28, "metric_value": 0.9403, "depth": 8}
								if obj[7]<=2:
									return 'True'
								elif obj[7]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Education", "instances": 92, "metric_value": 0.9109, "depth": 7}
							if obj[2]<=4:
								# {"feature": "Distance", "instances": 90, "metric_value": 0.8945, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							elif obj[2]>4:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Occupation", "instances": 191, "metric_value": 0.8919, "depth": 4}
				if obj[3]<=7.858638743455497:
					# {"feature": "Restaurant20to50", "instances": 111, "metric_value": 0.9631, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Education", "instances": 72, "metric_value": 0.9911, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Distance", "instances": 71, "metric_value": 0.993, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 59, "metric_value": 0.9898, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Distance", "instances": 39, "metric_value": 0.8582, "depth": 6}
						if obj[7]>1:
							# {"feature": "Education", "instances": 33, "metric_value": 0.9183, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 25, "metric_value": 0.8555, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]>2:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[7]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[3]>7.858638743455497:
					# {"feature": "Education", "instances": 80, "metric_value": 0.7219, "depth": 5}
					if obj[2]>0:
						# {"feature": "Restaurant20to50", "instances": 58, "metric_value": 0.8247, "depth": 6}
						if obj[5]>1.0:
							# {"feature": "Distance", "instances": 29, "metric_value": 0.9576, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 26, "metric_value": 0.9612, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]<=1.0:
							# {"feature": "Distance", "instances": 29, "metric_value": 0.5788, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 25, "metric_value": 0.5294, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.2668, "depth": 6}
						if obj[5]>0.0:
							return 'True'
						elif obj[5]<=0.0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[4]<=0.0:
			# {"feature": "Distance", "instances": 975, "metric_value": 0.8455, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Education", "instances": 797, "metric_value": 0.8733, "depth": 4}
				if obj[2]>0:
					# {"feature": "Occupation", "instances": 516, "metric_value": 0.8321, "depth": 5}
					if obj[3]<=12.343979481930436:
						# {"feature": "Restaurant20to50", "instances": 455, "metric_value": 0.8121, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Direction_same", "instances": 339, "metric_value": 0.8476, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Passanger", "instances": 254, "metric_value": 0.8324, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								# {"feature": "Passanger", "instances": 85, "metric_value": 0.8884, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[5]<=0.0:
							# {"feature": "Passanger", "instances": 116, "metric_value": 0.6823, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 101, "metric_value": 0.6305, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]>12.343979481930436:
						# {"feature": "Passanger", "instances": 61, "metric_value": 0.9432, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Restaurant20to50", "instances": 53, "metric_value": 0.9052, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 47, "metric_value": 0.8787, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 281, "metric_value": 0.933, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Occupation", "instances": 267, "metric_value": 0.9066, "depth": 6}
						if obj[3]<=10:
							# {"feature": "Passanger", "instances": 221, "metric_value": 0.9406, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 153, "metric_value": 0.9619, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 68, "metric_value": 0.874, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>10:
							# {"feature": "Direction_same", "instances": 46, "metric_value": 0.6153, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Passanger", "instances": 38, "metric_value": 0.6892, "depth": 8}
								if obj[0]<=2:
									return 'False'
								elif obj[0]>2:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>2.0:
						# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 6}
						if obj[3]>4:
							return 'True'
						elif obj[3]<=4:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[0]>2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>2:
				# {"feature": "Education", "instances": 178, "metric_value": 0.6796, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Occupation", "instances": 176, "metric_value": 0.6587, "depth": 5}
					if obj[3]<=11.790657263862823:
						# {"feature": "Passanger", "instances": 150, "metric_value": 0.5842, "depth": 6}
						if obj[0]>0:
							# {"feature": "Restaurant20to50", "instances": 137, "metric_value": 0.618, "depth": 7}
							if obj[5]>-1.0:
								# {"feature": "Direction_same", "instances": 134, "metric_value": 0.6264, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[3]>11.790657263862823:
						# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9306, "depth": 6}
						if obj[5]<=2.0:
							# {"feature": "Passanger", "instances": 24, "metric_value": 0.8709, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 22, "metric_value": 0.8454, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]>2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	else: return 'False'
