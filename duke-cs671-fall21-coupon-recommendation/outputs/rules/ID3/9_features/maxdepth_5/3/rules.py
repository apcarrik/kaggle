def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Restaurant20to50, obj[7]: Direction_same, obj[8]: Distance
	# {"feature": "Coupon", "instances": 8147, "metric_value": 0.985, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 5887, "metric_value": 0.9501, "depth": 2}
		if obj[8]<=2:
			# {"feature": "Passanger", "instances": 5324, "metric_value": 0.9337, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Restaurant20to50", "instances": 3124, "metric_value": 0.9594, "depth": 4}
				if obj[6]<=2.0:
					# {"feature": "Time", "instances": 2885, "metric_value": 0.9643, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Direction_same", "instances": 1819, "metric_value": 0.973, "depth": 6}
						if obj[7]>0:
							# {"feature": "Occupation", "instances": 980, "metric_value": 0.9403, "depth": 7}
							if obj[4]<=7.668367346938775:
								# {"feature": "Bar", "instances": 643, "metric_value": 0.9598, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Education", "instances": 636, "metric_value": 0.9573, "depth": 9}
									if obj[3]<=2:
										return 'True'
									elif obj[3]>2:
										return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[3]>1:
										return 'False'
									elif obj[3]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]>7.668367346938775:
								# {"feature": "Education", "instances": 337, "metric_value": 0.8916, "depth": 8}
								if obj[3]<=3:
									# {"feature": "Bar", "instances": 313, "metric_value": 0.8777, "depth": 9}
									if obj[5]<=3.0:
										return 'True'
									elif obj[5]>3.0:
										return 'True'
									else: return 'True'
								elif obj[3]>3:
									# {"feature": "Bar", "instances": 24, "metric_value": 0.995, "depth": 9}
									if obj[5]<=1.0:
										return 'True'
									elif obj[5]>1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=0:
							# {"feature": "Occupation", "instances": 839, "metric_value": 0.9948, "depth": 7}
							if obj[4]<=7.734207389749702:
								# {"feature": "Bar", "instances": 525, "metric_value": 0.9875, "depth": 8}
								if obj[5]<=3.0:
									# {"feature": "Education", "instances": 515, "metric_value": 0.9892, "depth": 9}
									if obj[3]<=4:
										return 'True'
									elif obj[3]>4:
										return 'True'
									else: return 'True'
								elif obj[5]>3.0:
									# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[3]<=2:
										return 'True'
									elif obj[3]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]>7.734207389749702:
								# {"feature": "Bar", "instances": 314, "metric_value": 1.0, "depth": 8}
								if obj[5]<=3.0:
									# {"feature": "Education", "instances": 308, "metric_value": 0.9997, "depth": 9}
									if obj[3]<=3:
										return 'True'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								elif obj[5]>3.0:
									# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[3]>0:
										return 'False'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]>1:
						# {"feature": "Direction_same", "instances": 1066, "metric_value": 0.9467, "depth": 6}
						if obj[7]<=0:
							# {"feature": "Education", "instances": 836, "metric_value": 0.9245, "depth": 7}
							if obj[3]<=4:
								# {"feature": "Bar", "instances": 834, "metric_value": 0.9253, "depth": 8}
								if obj[5]>-1.0:
									# {"feature": "Occupation", "instances": 822, "metric_value": 0.9231, "depth": 9}
									if obj[4]<=19.470563651438948:
										return 'True'
									elif obj[4]>19.470563651438948:
										return 'True'
									else: return 'True'
								elif obj[5]<=-1.0:
									# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 9}
									if obj[4]>1:
										return 'False'
									elif obj[4]<=1:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[3]>4:
								return 'True'
							else: return 'True'
						elif obj[7]>0:
							# {"feature": "Occupation", "instances": 230, "metric_value": 0.9945, "depth": 7}
							if obj[4]>0:
								# {"feature": "Education", "instances": 227, "metric_value": 0.996, "depth": 8}
								if obj[3]>1:
									# {"feature": "Bar", "instances": 138, "metric_value": 1.0, "depth": 9}
									if obj[5]<=1.0:
										return 'False'
									elif obj[5]>1.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=1:
									# {"feature": "Bar", "instances": 89, "metric_value": 0.9735, "depth": 9}
									if obj[5]>-1.0:
										return 'True'
									elif obj[5]<=-1.0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>2.0:
					# {"feature": "Occupation", "instances": 239, "metric_value": 0.8724, "depth": 5}
					if obj[4]<=18:
						# {"feature": "Time", "instances": 230, "metric_value": 0.8865, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 170, "metric_value": 0.9314, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Bar", "instances": 101, "metric_value": 0.8896, "depth": 8}
								if obj[5]<=2.0:
									# {"feature": "Direction_same", "instances": 86, "metric_value": 0.9103, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[5]>2.0:
									# {"feature": "Direction_same", "instances": 15, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]>2:
								# {"feature": "Bar", "instances": 69, "metric_value": 0.9742, "depth": 8}
								if obj[5]<=3.0:
									# {"feature": "Direction_same", "instances": 55, "metric_value": 0.9457, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[5]>3.0:
									# {"feature": "Direction_same", "instances": 14, "metric_value": 0.9852, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Direction_same", "instances": 60, "metric_value": 0.6873, "depth": 7}
							if obj[7]>0:
								# {"feature": "Bar", "instances": 30, "metric_value": 0.2108, "depth": 8}
								if obj[5]<=3.0:
									return 'True'
								elif obj[5]>3.0:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>2:
										return 'False'
									elif obj[3]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]<=0:
								# {"feature": "Bar", "instances": 30, "metric_value": 0.9183, "depth": 8}
								if obj[5]>1.0:
									# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 9}
									if obj[3]<=4:
										return 'False'
									elif obj[3]>4:
										return 'True'
									else: return 'True'
								elif obj[5]<=1.0:
									# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[4]>18:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Bar", "instances": 2200, "metric_value": 0.8857, "depth": 4}
				if obj[5]<=3.0:
					# {"feature": "Restaurant20to50", "instances": 2126, "metric_value": 0.8791, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Education", "instances": 1434, "metric_value": 0.903, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Occupation", "instances": 1345, "metric_value": 0.912, "depth": 7}
							if obj[4]>0:
								# {"feature": "Time", "instances": 1325, "metric_value": 0.9147, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 1020, "metric_value": 0.9173, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 305, "metric_value": 0.9058, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								# {"feature": "Time", "instances": 20, "metric_value": 0.6098, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]>3:
							# {"feature": "Occupation", "instances": 89, "metric_value": 0.7036, "depth": 7}
							if obj[4]<=21:
								# {"feature": "Time", "instances": 86, "metric_value": 0.6677, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 67, "metric_value": 0.608, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>3:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.8315, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]>21:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[6]>1.0:
						# {"feature": "Education", "instances": 692, "metric_value": 0.8203, "depth": 6}
						if obj[3]>1:
							# {"feature": "Occupation", "instances": 441, "metric_value": 0.8631, "depth": 7}
							if obj[4]>1:
								# {"feature": "Time", "instances": 407, "metric_value": 0.881, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Direction_same", "instances": 240, "metric_value": 0.8305, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 167, "metric_value": 0.937, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=1:
								# {"feature": "Time", "instances": 34, "metric_value": 0.5226, "depth": 8}
								if obj[1]<=2:
									return 'True'
								elif obj[1]>2:
									# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=1:
							# {"feature": "Occupation", "instances": 251, "metric_value": 0.7283, "depth": 7}
							if obj[4]>0:
								# {"feature": "Time", "instances": 246, "metric_value": 0.7363, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 197, "metric_value": 0.757, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 49, "metric_value": 0.6421, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[5]>3.0:
					# {"feature": "Occupation", "instances": 74, "metric_value": 0.9953, "depth": 5}
					if obj[4]<=14:
						# {"feature": "Time", "instances": 57, "metric_value": 0.973, "depth": 6}
						if obj[1]>0:
							# {"feature": "Education", "instances": 45, "metric_value": 0.9389, "depth": 7}
							if obj[3]>0:
								# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9784, "depth": 8}
								if obj[6]>0.0:
									# {"feature": "Direction_same", "instances": 28, "metric_value": 0.9852, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]>2.0:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									return 'True'
								else: return 'True'
							elif obj[6]>2.0:
								# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]>2:
									return 'False'
								elif obj[3]<=2:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[4]>14:
						# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 6}
						if obj[3]<=2:
							# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]<=1.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>2:
								# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[6]>1.0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[8]>2:
			# {"feature": "Passanger", "instances": 563, "metric_value": 0.9909, "depth": 3}
			if obj[0]>0:
				# {"feature": "Time", "instances": 546, "metric_value": 0.986, "depth": 4}
				if obj[1]>0:
					# {"feature": "Education", "instances": 473, "metric_value": 0.9973, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Bar", "instances": 431, "metric_value": 0.9928, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Occupation", "instances": 251, "metric_value": 0.9723, "depth": 7}
							if obj[4]>0:
								# {"feature": "Restaurant20to50", "instances": 249, "metric_value": 0.9741, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Direction_same", "instances": 247, "metric_value": 0.9759, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[6]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[5]<=0.0:
							# {"feature": "Restaurant20to50", "instances": 180, "metric_value": 0.9992, "depth": 7}
							if obj[6]>-1.0:
								# {"feature": "Occupation", "instances": 179, "metric_value": 0.9989, "depth": 8}
								if obj[4]>0:
									# {"feature": "Direction_same", "instances": 176, "metric_value": 0.9985, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[4]<=0:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=-1.0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>3:
						# {"feature": "Occupation", "instances": 42, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=11:
							# {"feature": "Bar", "instances": 34, "metric_value": 0.9774, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 24, "metric_value": 0.9183, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Direction_same", "instances": 23, "metric_value": 0.8865, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[6]>2.0:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[6]<=2.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[4]>11:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Bar", "instances": 73, "metric_value": 0.6759, "depth": 5}
					if obj[5]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 72, "metric_value": 0.65, "depth": 6}
						if obj[6]>0.0:
							# {"feature": "Occupation", "instances": 53, "metric_value": 0.7368, "depth": 7}
							if obj[4]<=20:
								# {"feature": "Education", "instances": 47, "metric_value": 0.785, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 30, "metric_value": 0.8813, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>2:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.5226, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[4]>20:
								return 'False'
							else: return 'False'
						elif obj[6]<=0.0:
							# {"feature": "Occupation", "instances": 19, "metric_value": 0.2975, "depth": 7}
							if obj[4]>2:
								return 'False'
							elif obj[4]<=2:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>3.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Occupation", "instances": 17, "metric_value": 0.5226, "depth": 4}
				if obj[4]>1:
					return 'True'
				elif obj[4]<=1:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]<=0.0:
						return 'True'
					elif obj[5]>0.0:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Bar", "instances": 2260, "metric_value": 0.9808, "depth": 2}
		if obj[5]<=1.0:
			# {"feature": "Occupation", "instances": 1577, "metric_value": 0.9216, "depth": 3}
			if obj[4]>1.8509661496426837:
				# {"feature": "Education", "instances": 1312, "metric_value": 0.9456, "depth": 4}
				if obj[3]>0:
					# {"feature": "Restaurant20to50", "instances": 846, "metric_value": 0.9085, "depth": 5}
					if obj[6]<=1.0:
						# {"feature": "Time", "instances": 599, "metric_value": 0.8736, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Distance", "instances": 366, "metric_value": 0.9183, "depth": 7}
							if obj[8]<=2:
								# {"feature": "Passanger", "instances": 273, "metric_value": 0.9506, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Direction_same", "instances": 252, "metric_value": 0.9436, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Direction_same", "instances": 21, "metric_value": 0.9984, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[8]>2:
								# {"feature": "Passanger", "instances": 93, "metric_value": 0.7706, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Direction_same", "instances": 92, "metric_value": 0.775, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[0]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[1]>2:
							# {"feature": "Passanger", "instances": 233, "metric_value": 0.7811, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Distance", "instances": 172, "metric_value": 0.6677, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 96, "metric_value": 0.6253, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 76, "metric_value": 0.7166, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Distance", "instances": 61, "metric_value": 0.967, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 47, "metric_value": 0.9441, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 14, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[6]>1.0:
						# {"feature": "Distance", "instances": 247, "metric_value": 0.969, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Time", "instances": 201, "metric_value": 0.9869, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 144, "metric_value": 0.9685, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Direction_same", "instances": 105, "metric_value": 0.9443, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[0]>2:
									# {"feature": "Direction_same", "instances": 39, "metric_value": 0.9995, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Passanger", "instances": 57, "metric_value": 0.998, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 49, "metric_value": 0.9997, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									# {"feature": "Direction_same", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[8]>2:
							# {"feature": "Passanger", "instances": 46, "metric_value": 0.7936, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 45, "metric_value": 0.7642, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 35, "metric_value": 0.7755, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Restaurant20to50", "instances": 466, "metric_value": 0.988, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Passanger", "instances": 441, "metric_value": 0.9833, "depth": 6}
						if obj[0]>0:
							# {"feature": "Time", "instances": 370, "metric_value": 0.974, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Distance", "instances": 309, "metric_value": 0.986, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 235, "metric_value": 0.9918, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[8]>2:
									# {"feature": "Direction_same", "instances": 74, "metric_value": 0.9569, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]>3:
								# {"feature": "Distance", "instances": 61, "metric_value": 0.8537, "depth": 8}
								if obj[8]<=1:
									# {"feature": "Direction_same", "instances": 33, "metric_value": 0.9673, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>1:
									# {"feature": "Direction_same", "instances": 28, "metric_value": 0.5917, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							# {"feature": "Time", "instances": 71, "metric_value": 0.9987, "depth": 7}
							if obj[1]>2:
								# {"feature": "Distance", "instances": 46, "metric_value": 0.9945, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 40, "metric_value": 0.9928, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>2:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]<=2:
								# {"feature": "Distance", "instances": 25, "metric_value": 0.9427, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>2.0:
						# {"feature": "Passanger", "instances": 25, "metric_value": 0.9427, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 21, "metric_value": 0.9852, "depth": 7}
							if obj[1]<=2:
								# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]>2:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>2:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]>1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]<=1.8509661496426837:
				# {"feature": "Restaurant20to50", "instances": 265, "metric_value": 0.7294, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Distance", "instances": 216, "metric_value": 0.7885, "depth": 5}
					if obj[8]<=2:
						# {"feature": "Education", "instances": 177, "metric_value": 0.8266, "depth": 6}
						if obj[3]>0:
							# {"feature": "Passanger", "instances": 121, "metric_value": 0.7659, "depth": 7}
							if obj[0]<=2:
								# {"feature": "Time", "instances": 96, "metric_value": 0.7177, "depth": 8}
								if obj[1]>0:
									# {"feature": "Direction_same", "instances": 67, "metric_value": 0.6442, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Direction_same", "instances": 29, "metric_value": 0.8498, "depth": 9}
									if obj[7]>0:
										return 'False'
									elif obj[7]<=0:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[0]>2:
								# {"feature": "Time", "instances": 25, "metric_value": 0.9044, "depth": 8}
								if obj[1]>2:
									# {"feature": "Direction_same", "instances": 20, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]<=2:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 56, "metric_value": 0.9241, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Time", "instances": 35, "metric_value": 0.971, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 31, "metric_value": 0.9383, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]>1:
								# {"feature": "Time", "instances": 21, "metric_value": 0.7919, "depth": 8}
								if obj[1]<=3:
									# {"feature": "Direction_same", "instances": 18, "metric_value": 0.8524, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[1]>3:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[8]>2:
						# {"feature": "Passanger", "instances": 39, "metric_value": 0.5525, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 38, "metric_value": 0.4855, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 32, "metric_value": 0.5436, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 30, "metric_value": 0.5665, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[3]>2:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[6]<=0.0:
					# {"feature": "Education", "instances": 49, "metric_value": 0.3323, "depth": 5}
					if obj[3]<=4:
						return 'False'
					elif obj[3]>4:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[5]>1.0:
			# {"feature": "Restaurant20to50", "instances": 683, "metric_value": 0.9663, "depth": 3}
			if obj[6]<=2.0:
				# {"feature": "Passanger", "instances": 562, "metric_value": 0.9838, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Time", "instances": 474, "metric_value": 0.9938, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Occupation", "instances": 308, "metric_value": 0.9724, "depth": 6}
						if obj[4]>0:
							# {"feature": "Direction_same", "instances": 304, "metric_value": 0.9754, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Distance", "instances": 215, "metric_value": 0.9886, "depth": 8}
								if obj[8]>1:
									# {"feature": "Education", "instances": 206, "metric_value": 0.9825, "depth": 9}
									if obj[3]<=4:
										return 'True'
									elif obj[3]>4:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 9}
									if obj[3]<=3:
										return 'False'
									elif obj[3]>3:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[7]>0:
								# {"feature": "Education", "instances": 89, "metric_value": 0.922, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Distance", "instances": 77, "metric_value": 0.8951, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 9}
									if obj[8]<=1:
										return 'True'
									elif obj[8]>1:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[4]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						# {"feature": "Occupation", "instances": 166, "metric_value": 0.9933, "depth": 6}
						if obj[4]<=8.74698795180723:
							# {"feature": "Education", "instances": 97, "metric_value": 0.9659, "depth": 7}
							if obj[3]>0:
								# {"feature": "Distance", "instances": 65, "metric_value": 0.9861, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 62, "metric_value": 0.9932, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								elif obj[8]>2:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Distance", "instances": 32, "metric_value": 0.896, "depth": 8}
								if obj[8]<=2:
									# {"feature": "Direction_same", "instances": 31, "metric_value": 0.8691, "depth": 9}
									if obj[7]<=0:
										return 'False'
									else: return 'False'
								elif obj[8]>2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>8.74698795180723:
							# {"feature": "Distance", "instances": 69, "metric_value": 0.9962, "depth": 7}
							if obj[8]<=1:
								# {"feature": "Education", "instances": 44, "metric_value": 0.9624, "depth": 8}
								if obj[3]<=1:
									# {"feature": "Direction_same", "instances": 22, "metric_value": 0.9024, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[3]>1:
									# {"feature": "Direction_same", "instances": 22, "metric_value": 0.994, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[8]>1:
								# {"feature": "Education", "instances": 25, "metric_value": 0.971, "depth": 8}
								if obj[3]<=2:
									# {"feature": "Direction_same", "instances": 19, "metric_value": 0.998, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[3]>2:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[7]<=0:
										return 'False'
									elif obj[7]>0:
										return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'False'
				elif obj[0]>2:
					# {"feature": "Time", "instances": 88, "metric_value": 0.8454, "depth": 5}
					if obj[1]>2:
						# {"feature": "Education", "instances": 67, "metric_value": 0.6442, "depth": 6}
						if obj[3]>1:
							# {"feature": "Occupation", "instances": 37, "metric_value": 0.8004, "depth": 7}
							if obj[4]>4:
								# {"feature": "Distance", "instances": 23, "metric_value": 0.6666, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 17, "metric_value": 0.6723, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=4:
								# {"feature": "Distance", "instances": 14, "metric_value": 0.9403, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[3]<=1:
							# {"feature": "Occupation", "instances": 30, "metric_value": 0.3534, "depth": 7}
							if obj[4]>6:
								# {"feature": "Distance", "instances": 18, "metric_value": 0.5033, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3912, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[4]<=6:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=2:
						# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 6}
						if obj[4]<=12:
							# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 7}
							if obj[3]<=2:
								# {"feature": "Direction_same", "instances": 13, "metric_value": 0.7793, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.7793, "depth": 9}
									if obj[8]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[3]>2:
								return 'False'
							else: return 'False'
						elif obj[4]>12:
							# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[3]>1:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[6]>2.0:
				# {"feature": "Occupation", "instances": 121, "metric_value": 0.7945, "depth": 4}
				if obj[4]<=9:
					# {"feature": "Education", "instances": 77, "metric_value": 0.655, "depth": 5}
					if obj[3]>0:
						# {"feature": "Time", "instances": 69, "metric_value": 0.5586, "depth": 6}
						if obj[1]>0:
							# {"feature": "Direction_same", "instances": 52, "metric_value": 0.6647, "depth": 7}
							if obj[7]<=0:
								# {"feature": "Passanger", "instances": 48, "metric_value": 0.5993, "depth": 8}
								if obj[0]>0:
									# {"feature": "Distance", "instances": 44, "metric_value": 0.6321, "depth": 9}
									if obj[8]>1:
										return 'True'
									elif obj[8]<=1:
										return 'True'
									else: return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[7]>0:
								# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[8]<=1:
									return 'False'
								elif obj[8]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[8]>1:
									# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									else: return 'True'
								elif obj[8]<=1:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>9:
					# {"feature": "Education", "instances": 44, "metric_value": 0.9457, "depth": 5}
					if obj[3]<=2:
						# {"feature": "Distance", "instances": 30, "metric_value": 0.8813, "depth": 6}
						if obj[8]<=2:
							# {"feature": "Passanger", "instances": 27, "metric_value": 0.9183, "depth": 7}
							if obj[0]>0:
								# {"feature": "Time", "instances": 25, "metric_value": 0.8555, "depth": 8}
								if obj[1]>1:
									# {"feature": "Direction_same", "instances": 15, "metric_value": 0.9183, "depth": 9}
									if obj[7]<=0:
										return 'True'
									elif obj[7]>0:
										return 'True'
									else: return 'True'
								elif obj[1]<=1:
									# {"feature": "Direction_same", "instances": 10, "metric_value": 0.7219, "depth": 9}
									if obj[7]>0:
										return 'True'
									elif obj[7]<=0:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						elif obj[8]>2:
							return 'True'
						else: return 'True'
					elif obj[3]>2:
						# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[8]>1:
							# {"feature": "Time", "instances": 12, "metric_value": 0.9799, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 10, "metric_value": 1.0, "depth": 8}
								if obj[7]<=0:
									# {"feature": "Passanger", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										return 'True'
									else: return 'True'
								elif obj[7]>0:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[8]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
