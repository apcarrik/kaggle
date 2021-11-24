def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Age", "instances": 96, "metric_value": 0.9997, "depth": 2}
		if obj[4]<=3:
			# {"feature": "Coupon", "instances": 52, "metric_value": 0.9829, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Occupation", "instances": 29, "metric_value": 0.9991, "depth": 4}
				if obj[7]>1:
					# {"feature": "Gender", "instances": 24, "metric_value": 0.9799, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Bar", "instances": 16, "metric_value": 0.896, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Direction_same", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[11]<=0:
								# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[12]<=2:
									# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[1]>0:
										# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5]<=0:
											# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]>0.0:
												return 'False'
											elif obj[9]<=0.0:
												return 'True'
											else: return 'True'
										elif obj[5]>0:
											return 'True'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								elif obj[12]>2:
									return 'False'
								else: return 'False'
							elif obj[11]>0:
								return 'False'
							else: return 'False'
						elif obj[8]>2.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=2:
									return 'True'
								elif obj[6]>2:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[11]<=0:
										return 'True'
									elif obj[11]>0:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[10]<=1.0:
							# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[6]>1:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]>0:
									# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=0:
										return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[6]<=1:
								return 'False'
							else: return 'False'
						elif obj[10]>1.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[7]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[7]>1:
						# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9968, "depth": 6}
						if obj[9]>0.0:
							# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[1]>0:
								# {"feature": "Children", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[5]>0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]<=2.0:
										return 'True'
									elif obj[10]>2.0:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[10]>0.0:
										return 'False'
									elif obj[10]<=0.0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						elif obj[9]<=0.0:
							# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[1]>0:
								return 'False'
							elif obj[1]<=0:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'False'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>3:
			# {"feature": "Distance", "instances": 44, "metric_value": 0.9624, "depth": 3}
			if obj[12]<=2:
				# {"feature": "Coffeehouse", "instances": 38, "metric_value": 0.8997, "depth": 4}
				if obj[9]<=3.0:
					# {"feature": "Bar", "instances": 36, "metric_value": 0.8524, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9294, "depth": 6}
						if obj[10]<=2.0:
							# {"feature": "Education", "instances": 27, "metric_value": 0.951, "depth": 7}
							if obj[6]>0:
								# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 8}
								if obj[2]>0:
									# {"feature": "Children", "instances": 14, "metric_value": 0.5917, "depth": 9}
									if obj[5]<=0:
										# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[1]>0:
											# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[3]>0:
												# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 12}
												if obj[7]>1:
													# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 13}
													if obj[11]<=0:
														return 'True'
													elif obj[11]>0:
														return 'True'
													else: return 'True'
												elif obj[7]<=1:
													return 'True'
												else: return 'True'
											elif obj[3]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]<=0:
											return 'True'
										else: return 'True'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								elif obj[2]<=0:
									# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[1]>2:
										# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]>4:
											return 'True'
										elif obj[7]<=4:
											return 'False'
										else: return 'False'
									elif obj[1]<=2:
										return 'False'
									else: return 'False'
								else: return 'False'
							elif obj[6]<=0:
								# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]>2:
										# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=2:
											# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[2]>2:
												# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]<=1:
														return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[2]<=2:
												return 'True'
											else: return 'True'
										elif obj[1]>2:
											return 'False'
										else: return 'False'
									elif obj[7]<=2:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[10]>2.0:
							return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						return 'True'
					else: return 'True'
				elif obj[9]>3.0:
					return 'False'
				else: return 'False'
			elif obj[12]>2:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[8]<=0.0:
					return 'False'
				elif obj[8]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.5548, "depth": 2}
		if obj[7]>6:
			# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Children", "instances": 11, "metric_value": 0.9457, "depth": 4}
				if obj[5]<=0:
					# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[8]<=1.0:
						return 'True'
					elif obj[8]>1.0:
						return 'False'
					else: return 'False'
				elif obj[5]>0:
					# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[8]<=1.0:
						return 'False'
					elif obj[8]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]>2.0:
				return 'True'
			else: return 'True'
		elif obj[7]<=6:
			return 'True'
		else: return 'True'
	else: return 'True'
