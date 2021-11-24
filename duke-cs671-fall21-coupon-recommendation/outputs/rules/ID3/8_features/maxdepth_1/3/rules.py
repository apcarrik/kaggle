def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.985, "depth": 1}
	if obj[1]>1:
		# {"feature": "Distance", "instances": 5887, "metric_value": 0.9501, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Passanger", "instances": 5324, "metric_value": 0.9337, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 3124, "metric_value": 0.9594, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Occupation", "instances": 2885, "metric_value": 0.9643, "depth": 5}
					if obj[3]>0:
						# {"feature": "Bar", "instances": 2851, "metric_value": 0.9655, "depth": 6}
						if obj[4]>-1.0:
							# {"feature": "Direction_same", "instances": 2824, "metric_value": 0.9647, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Education", "instances": 1634, "metric_value": 0.9707, "depth": 8}
								if obj[2]<=4:
									return 'True'
								elif obj[2]>4:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								# {"feature": "Education", "instances": 1190, "metric_value": 0.9555, "depth": 8}
								if obj[2]<=2:
									return 'True'
								elif obj[2]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]<=-1.0:
							# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 7}
							if obj[2]>1:
								# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=1:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[3]<=0:
						# {"feature": "Direction_same", "instances": 34, "metric_value": 0.7871, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Bar", "instances": 22, "metric_value": 0.9024, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 8}
								if obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[2]>0:
									return 'True'
								elif obj[2]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							# {"feature": "Bar", "instances": 12, "metric_value": 0.4138, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[2]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>2.0:
					# {"feature": "Occupation", "instances": 239, "metric_value": 0.8724, "depth": 5}
					if obj[3]<=18:
						# {"feature": "Bar", "instances": 230, "metric_value": 0.8865, "depth": 6}
						if obj[4]<=3.0:
							# {"feature": "Education", "instances": 200, "metric_value": 0.8555, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 137, "metric_value": 0.8892, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 63, "metric_value": 0.7642, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[4]>3.0:
							# {"feature": "Education", "instances": 30, "metric_value": 0.9968, "depth": 7}
							if obj[2]>2:
								# {"feature": "Direction_same", "instances": 18, "metric_value": 0.9641, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[2]<=2:
								# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Bar", "instances": 2200, "metric_value": 0.8857, "depth": 4}
				if obj[4]<=3.0:
					# {"feature": "Restaurant20to50", "instances": 2126, "metric_value": 0.8791, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Education", "instances": 1434, "metric_value": 0.903, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Occupation", "instances": 1345, "metric_value": 0.912, "depth": 7}
							if obj[3]>0:
								# {"feature": "Direction_same", "instances": 1325, "metric_value": 0.9147, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Direction_same", "instances": 20, "metric_value": 0.6098, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							# {"feature": "Occupation", "instances": 89, "metric_value": 0.7036, "depth": 7}
							if obj[3]<=21:
								# {"feature": "Direction_same", "instances": 86, "metric_value": 0.6677, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]>21:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>1.0:
						# {"feature": "Education", "instances": 692, "metric_value": 0.8203, "depth": 6}
						if obj[2]>1:
							# {"feature": "Occupation", "instances": 441, "metric_value": 0.8631, "depth": 7}
							if obj[3]>1:
								# {"feature": "Direction_same", "instances": 407, "metric_value": 0.881, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Direction_same", "instances": 34, "metric_value": 0.5226, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]<=1:
							# {"feature": "Occupation", "instances": 251, "metric_value": 0.7283, "depth": 7}
							if obj[3]>0:
								# {"feature": "Direction_same", "instances": 246, "metric_value": 0.7363, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>3.0:
					# {"feature": "Occupation", "instances": 74, "metric_value": 0.9953, "depth": 5}
					if obj[3]<=14:
						# {"feature": "Restaurant20to50", "instances": 57, "metric_value": 0.973, "depth": 6}
						if obj[5]>2.0:
							# {"feature": "Education", "instances": 30, "metric_value": 0.9968, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 22, "metric_value": 0.994, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=2.0:
							# {"feature": "Education", "instances": 27, "metric_value": 0.9183, "depth": 7}
							if obj[2]>0:
								# {"feature": "Direction_same", "instances": 16, "metric_value": 0.9887, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[3]>14:
						# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 7}
							if obj[5]>1.0:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[7]>2:
			# {"feature": "Passanger", "instances": 563, "metric_value": 0.9909, "depth": 3}
			if obj[0]>0:
				# {"feature": "Bar", "instances": 546, "metric_value": 0.986, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Education", "instances": 319, "metric_value": 0.964, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Occupation", "instances": 290, "metric_value": 0.9525, "depth": 6}
						if obj[3]>0:
							# {"feature": "Restaurant20to50", "instances": 288, "metric_value": 0.9544, "depth": 7}
							if obj[5]>-1.0:
								# {"feature": "Direction_same", "instances": 286, "metric_value": 0.9563, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[5]<=-1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>3:
						# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 6}
						if obj[3]<=6:
							# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.9774, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9911, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>6:
							# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[5]<=0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=0.0:
					# {"feature": "Education", "instances": 227, "metric_value": 0.9997, "depth": 5}
					if obj[2]<=4:
						# {"feature": "Restaurant20to50", "instances": 225, "metric_value": 0.9993, "depth": 6}
						if obj[5]>-1.0:
							# {"feature": "Occupation", "instances": 223, "metric_value": 0.9996, "depth": 7}
							if obj[3]<=7.291479820627803:
								# {"feature": "Direction_same", "instances": 153, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]>7.291479820627803:
								# {"feature": "Direction_same", "instances": 70, "metric_value": 0.9947, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[5]<=-1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>4:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.5226, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=0.0:
						return 'True'
					elif obj[4]>0.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Bar", "instances": 2260, "metric_value": 0.9808, "depth": 2}
		if obj[4]<=1.0:
			# {"feature": "Occupation", "instances": 1577, "metric_value": 0.9216, "depth": 3}
			if obj[3]>1.8509661496426837:
				# {"feature": "Education", "instances": 1312, "metric_value": 0.9456, "depth": 4}
				if obj[2]>0:
					# {"feature": "Restaurant20to50", "instances": 846, "metric_value": 0.9085, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Passanger", "instances": 599, "metric_value": 0.8736, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 517, "metric_value": 0.8481, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Direction_same", "instances": 415, "metric_value": 0.8645, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]>2:
								# {"feature": "Direction_same", "instances": 102, "metric_value": 0.7701, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							# {"feature": "Distance", "instances": 82, "metric_value": 0.9789, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 68, "metric_value": 0.9692, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>1.0:
						# {"feature": "Distance", "instances": 247, "metric_value": 0.969, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Passanger", "instances": 201, "metric_value": 0.9869, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 178, "metric_value": 0.9794, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9877, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]>2:
							# {"feature": "Passanger", "instances": 46, "metric_value": 0.7936, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 45, "metric_value": 0.7642, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[2]<=0:
					# {"feature": "Restaurant20to50", "instances": 466, "metric_value": 0.988, "depth": 5}
					if obj[5]<=2.0:
						# {"feature": "Passanger", "instances": 441, "metric_value": 0.9833, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 370, "metric_value": 0.974, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Direction_same", "instances": 296, "metric_value": 0.9776, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[7]>2:
								# {"feature": "Direction_same", "instances": 74, "metric_value": 0.9569, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Distance", "instances": 71, "metric_value": 0.9987, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Direction_same", "instances": 43, "metric_value": 0.9965, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>1:
								# {"feature": "Direction_same", "instances": 28, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]>2.0:
						# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Distance", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[7]>2:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]<=1.8509661496426837:
				# {"feature": "Restaurant20to50", "instances": 265, "metric_value": 0.7294, "depth": 4}
				if obj[5]>0.0:
					# {"feature": "Distance", "instances": 216, "metric_value": 0.7885, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Education", "instances": 177, "metric_value": 0.8266, "depth": 6}
						if obj[2]>0:
							# {"feature": "Passanger", "instances": 121, "metric_value": 0.7659, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Direction_same", "instances": 96, "metric_value": 0.7177, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Direction_same", "instances": 25, "metric_value": 0.9044, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Passanger", "instances": 56, "metric_value": 0.9241, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Direction_same", "instances": 35, "metric_value": 0.971, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[0]>1:
								# {"feature": "Direction_same", "instances": 21, "metric_value": 0.7919, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[7]>2:
						# {"feature": "Passanger", "instances": 39, "metric_value": 0.5525, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 38, "metric_value": 0.4855, "depth": 7}
							if obj[2]<=2:
								# {"feature": "Direction_same", "instances": 36, "metric_value": 0.5033, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[2]>2:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]<=0.0:
					# {"feature": "Education", "instances": 49, "metric_value": 0.3323, "depth": 5}
					if obj[2]<=4:
						return 'False'
					elif obj[2]>4:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'False'
								else: return 'False'
							elif obj[6]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[4]>1.0:
			# {"feature": "Restaurant20to50", "instances": 683, "metric_value": 0.9663, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Passanger", "instances": 562, "metric_value": 0.9838, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Direction_same", "instances": 474, "metric_value": 0.9938, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Occupation", "instances": 377, "metric_value": 0.9989, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 374, "metric_value": 0.9993, "depth": 7}
							if obj[7]<=2:
								# {"feature": "Education", "instances": 274, "metric_value": 0.9998, "depth": 8}
								if obj[2]<=4:
									return 'False'
								elif obj[2]>4:
									return 'True'
								else: return 'True'
							elif obj[7]>2:
								# {"feature": "Education", "instances": 100, "metric_value": 0.9815, "depth": 8}
								if obj[2]<=2:
									return 'True'
								elif obj[2]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>0:
						# {"feature": "Education", "instances": 97, "metric_value": 0.9345, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Occupation", "instances": 83, "metric_value": 0.8969, "depth": 7}
							if obj[3]>1:
								# {"feature": "Distance", "instances": 71, "metric_value": 0.9359, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>2:
							# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 7}
							if obj[7]<=1:
								# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[3]<=14:
									return 'True'
								elif obj[3]>14:
									return 'False'
								else: return 'False'
							elif obj[7]>1:
								# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[3]<=6:
									return 'False'
								elif obj[3]>6:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>2:
					# {"feature": "Education", "instances": 88, "metric_value": 0.8454, "depth": 5}
					if obj[2]>1:
						# {"feature": "Occupation", "instances": 51, "metric_value": 0.9526, "depth": 6}
						if obj[3]>0:
							# {"feature": "Distance", "instances": 50, "metric_value": 0.9427, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 41, "metric_value": 0.965, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						# {"feature": "Occupation", "instances": 37, "metric_value": 0.5714, "depth": 6}
						if obj[3]>6:
							# {"feature": "Distance", "instances": 24, "metric_value": 0.7383, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 19, "metric_value": 0.7425, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=6:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				# {"feature": "Occupation", "instances": 121, "metric_value": 0.7945, "depth": 4}
				if obj[3]<=9:
					# {"feature": "Education", "instances": 77, "metric_value": 0.655, "depth": 5}
					if obj[2]>0:
						# {"feature": "Passanger", "instances": 69, "metric_value": 0.5586, "depth": 6}
						if obj[0]>0:
							# {"feature": "Distance", "instances": 64, "metric_value": 0.5859, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 41, "metric_value": 0.5349, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[7]<=1:
								# {"feature": "Direction_same", "instances": 23, "metric_value": 0.6666, "depth": 8}
								if obj[6]>0:
									return 'True'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[7]>1:
								# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>9:
					# {"feature": "Education", "instances": 44, "metric_value": 0.9457, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Distance", "instances": 30, "metric_value": 0.8813, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Passanger", "instances": 27, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								# {"feature": "Direction_same", "instances": 25, "metric_value": 0.8555, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]>2:
							return 'True'
						else: return 'True'
					elif obj[2]>2:
						# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[7]>1:
							# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[0]<=1:
									return 'True'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[6]>0:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
