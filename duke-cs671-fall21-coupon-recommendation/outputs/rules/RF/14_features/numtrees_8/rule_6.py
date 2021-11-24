def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coffeehouse", "instances": 95, "metric_value": 0.8748, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Bar", "instances": 79, "metric_value": 0.7742, "depth": 3}
			if obj[9]<=2.0:
				# {"feature": "Education", "instances": 68, "metric_value": 0.8338, "depth": 4}
				if obj[6]<=3:
					# {"feature": "Income", "instances": 62, "metric_value": 0.8691, "depth": 5}
					if obj[8]>3:
						# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.684, "depth": 6}
						if obj[11]<=1.0:
							# {"feature": "Occupation", "instances": 21, "metric_value": 0.8631, "depth": 7}
							if obj[7]<=6:
								# {"feature": "Children", "instances": 11, "metric_value": 0.994, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Direction_same", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[12]<=0:
										# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[13]<=2:
											return 'False'
										elif obj[13]>2:
											return 'True'
										else: return 'True'
									elif obj[12]>0:
										return 'True'
									else: return 'True'
								elif obj[5]>0:
									# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[4]>1:
												return 'False'
											elif obj[4]<=1:
												return 'True'
											else: return 'True'
										elif obj[3]>0:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[7]>6:
								# {"feature": "Age", "instances": 10, "metric_value": 0.469, "depth": 8}
								if obj[4]>0:
									return 'True'
								elif obj[4]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]>1.0:
							return 'True'
						else: return 'True'
					elif obj[8]<=3:
						# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9784, "depth": 6}
						if obj[11]<=2.0:
							# {"feature": "Gender", "instances": 26, "metric_value": 0.9957, "depth": 7}
							if obj[3]>0:
								# {"feature": "Children", "instances": 15, "metric_value": 0.971, "depth": 8}
								if obj[5]>0:
									# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 9}
									if obj[1]>1:
										# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[0]>1:
											# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[7]<=7:
												return 'False'
											elif obj[7]>7:
												return 'True'
											else: return 'True'
										elif obj[0]<=1:
											return 'False'
										else: return 'False'
									elif obj[1]<=1:
										# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[4]>0:
											return 'True'
										elif obj[4]<=0:
											# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[7]<=2:
												return 'True'
											elif obj[7]>2:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'True'
								elif obj[5]<=0:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 8}
								if obj[13]>1:
									# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[7]>2:
										# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 11}
											if obj[1]>0:
												# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[4]>3:
													# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]<=0:
														# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[12]<=0:
															return 'False'
														else: return 'False'
													else: return 'False'
												elif obj[4]<=3:
													return 'False'
												else: return 'False'
											elif obj[1]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									elif obj[7]<=2:
										return 'False'
									else: return 'False'
								elif obj[13]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[11]>2.0:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>3:
					return 'True'
				else: return 'True'
			elif obj[9]>2.0:
				return 'True'
			else: return 'True'
		elif obj[10]<=0.0:
			# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[13]>1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[13]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		# {"feature": "Income", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[8]<=4:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[7]>2:
				# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=3:
					# {"feature": "Gender", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=2.0:
								return 'False'
							elif obj[10]>2.0:
								return 'True'
							else: return 'True'
						elif obj[4]>2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[6]>3:
					return 'True'
				else: return 'True'
			elif obj[7]<=2:
				return 'True'
			else: return 'True'
		elif obj[8]>4:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[7]<=12:
				return 'False'
			elif obj[7]>12:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
