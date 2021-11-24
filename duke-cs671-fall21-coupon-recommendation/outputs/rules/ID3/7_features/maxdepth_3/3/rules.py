def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.985, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5887, "metric_value": 0.9501, "depth": 2}
		if obj[6]<=2:
			# {"feature": "Passanger", "instances": 5324, "metric_value": 0.9337, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 3124, "metric_value": 0.9594, "depth": 4}
				if obj[4]<=2.0:
					# {"feature": "Occupation", "instances": 2885, "metric_value": 0.9643, "depth": 5}
					if obj[3]>0:
						# {"feature": "Direction_same", "instances": 2851, "metric_value": 0.9655, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 1653, "metric_value": 0.9709, "depth": 7}
							if obj[2]<=4:
								return 'True'
							elif obj[2]>4:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 1198, "metric_value": 0.9573, "depth": 7}
							if obj[2]<=2:
								return 'True'
							elif obj[2]>2:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Direction_same", "instances": 34, "metric_value": 0.7871, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Education", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Education", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if obj[2]<=0:
								return 'True'
							elif obj[2]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>2.0:
					# {"feature": "Occupation", "instances": 239, "metric_value": 0.8724, "depth": 5}
					if obj[3]<=18:
						# {"feature": "Education", "instances": 230, "metric_value": 0.8865, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Direction_same", "instances": 141, "metric_value": 0.8304, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						elif obj[2]>2:
							# {"feature": "Direction_same", "instances": 89, "metric_value": 0.9513, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Restaurant20to50", "instances": 2200, "metric_value": 0.8857, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Education", "instances": 1458, "metric_value": 0.9047, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Occupation", "instances": 1364, "metric_value": 0.9133, "depth": 6}
						if obj[3]>0:
							# {"feature": "Direction_same", "instances": 1344, "metric_value": 0.916, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Direction_same", "instances": 20, "metric_value": 0.6098, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Occupation", "instances": 94, "metric_value": 0.7262, "depth": 6}
						if obj[3]<=21:
							# {"feature": "Direction_same", "instances": 91, "metric_value": 0.6948, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>21:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>1.0:
					# {"feature": "Education", "instances": 742, "metric_value": 0.8427, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 478, "metric_value": 0.8878, "depth": 6}
						if obj[3]<=20:
							# {"feature": "Direction_same", "instances": 464, "metric_value": 0.8754, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]>20:
							# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9403, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 264, "metric_value": 0.7383, "depth": 6}
						if obj[3]>0:
							# {"feature": "Direction_same", "instances": 259, "metric_value": 0.746, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>2:
			# {"feature": "Passanger", "instances": 563, "metric_value": 0.9909, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 546, "metric_value": 0.986, "depth": 4}
				if obj[2]<=4:
					# {"feature": "Restaurant20to50", "instances": 543, "metric_value": 0.9847, "depth": 5}
					if obj[4]>-1.0:
						# {"feature": "Occupation", "instances": 539, "metric_value": 0.986, "depth": 6}
						if obj[3]>0:
							# {"feature": "Direction_same", "instances": 534, "metric_value": 0.9868, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[2]>4:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.5226, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]>0:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Restaurant20to50", "instances": 2260, "metric_value": 0.9808, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 1494, "metric_value": 0.9498, "depth": 3}
			if obj[3]>1.9106811377923965:
				# {"feature": "Education", "instances": 1245, "metric_value": 0.965, "depth": 4}
				if obj[2]>0:
					# {"feature": "Passanger", "instances": 799, "metric_value": 0.9388, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Direction_same", "instances": 683, "metric_value": 0.9173, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 544, "metric_value": 0.9062, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 139, "metric_value": 0.9538, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>2:
						# {"feature": "Distance", "instances": 116, "metric_value": 0.9998, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 96, "metric_value": 0.9987, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9928, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Passanger", "instances": 446, "metric_value": 0.9936, "depth": 5}
					if obj[0]>0:
						# {"feature": "Direction_same", "instances": 384, "metric_value": 0.9896, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 304, "metric_value": 0.9862, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 80, "metric_value": 0.9982, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]<=0:
						# {"feature": "Distance", "instances": 62, "metric_value": 0.997, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 57, "metric_value": 0.998, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=1.9106811377923965:
				# {"feature": "Education", "instances": 249, "metric_value": 0.8283, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Direction_same", "instances": 227, "metric_value": 0.7988, "depth": 5}
					if obj[5]<=0:
						# {"feature": "Passanger", "instances": 174, "metric_value": 0.7355, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 138, "metric_value": 0.65, "depth": 7}
							if obj[6]<=2:
								return 'False'
							elif obj[6]>2:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Distance", "instances": 36, "metric_value": 0.9436, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>0:
						# {"feature": "Passanger", "instances": 53, "metric_value": 0.9414, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 49, "metric_value": 0.9313, "depth": 7}
							if obj[6]<=1:
								return 'False'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[6]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Passanger", "instances": 22, "metric_value": 0.994, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Distance", "instances": 19, "metric_value": 0.9495, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]<=1:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Passanger", "instances": 766, "metric_value": 0.9993, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 651, "metric_value": 0.9999, "depth": 4}
				if obj[3]<=8.23041474654378:
					# {"feature": "Education", "instances": 391, "metric_value": 0.9966, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Distance", "instances": 357, "metric_value": 0.9938, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 281, "metric_value": 0.9979, "depth": 7}
							if obj[5]<=0:
								return 'False'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							# {"feature": "Direction_same", "instances": 76, "metric_value": 0.9591, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]>3:
						# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9774, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 22, "metric_value": 0.9457, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>8.23041474654378:
					# {"feature": "Education", "instances": 260, "metric_value": 0.9957, "depth": 5}
					if obj[2]>1:
						# {"feature": "Direction_same", "instances": 161, "metric_value": 0.9993, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 130, "metric_value": 0.9916, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 31, "metric_value": 0.9383, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[2]<=1:
						# {"feature": "Direction_same", "instances": 99, "metric_value": 0.9535, "depth": 6}
						if obj[5]<=0:
							# {"feature": "Distance", "instances": 79, "metric_value": 0.9663, "depth": 7}
							if obj[6]>1:
								return 'True'
							elif obj[6]<=1:
								return 'True'
							else: return 'True'
						elif obj[5]>0:
							# {"feature": "Distance", "instances": 20, "metric_value": 0.8813, "depth": 7}
							if obj[6]<=1:
								return 'True'
							elif obj[6]>1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 115, "metric_value": 0.9469, "depth": 4}
				if obj[2]>0:
					# {"feature": "Distance", "instances": 82, "metric_value": 0.9892, "depth": 5}
					if obj[6]>1:
						# {"feature": "Occupation", "instances": 73, "metric_value": 0.9988, "depth": 6}
						if obj[3]<=6:
							# {"feature": "Direction_same", "instances": 42, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[3]>6:
							# {"feature": "Direction_same", "instances": 31, "metric_value": 0.9383, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]<=1:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[3]>5:
							return 'True'
						elif obj[3]<=5:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[2]<=0:
					# {"feature": "Occupation", "instances": 33, "metric_value": 0.684, "depth": 5}
					if obj[3]<=6:
						# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 16, "metric_value": 0.896, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]>6:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
