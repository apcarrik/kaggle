def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Age", "instances": 84, "metric_value": 0.9934, "depth": 2}
		if obj[6]>1:
			# {"feature": "Bar", "instances": 58, "metric_value": 0.9294, "depth": 3}
			if obj[12]<=2.0:
				# {"feature": "Distance", "instances": 52, "metric_value": 0.9612, "depth": 4}
				if obj[16]<=2:
					# {"feature": "Occupation", "instances": 39, "metric_value": 0.9957, "depth": 5}
					if obj[10]>2:
						# {"feature": "Income", "instances": 32, "metric_value": 0.9544, "depth": 6}
						if obj[11]>2:
							# {"feature": "Education", "instances": 26, "metric_value": 0.9957, "depth": 7}
							if obj[9]>0:
								# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9183, "depth": 8}
								if obj[13]<=2.0:
									# {"feature": "Time", "instances": 15, "metric_value": 0.971, "depth": 9}
									if obj[2]>0:
										# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 10}
										if obj[3]<=3:
											# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[14]>1.0:
												# {"feature": "Maritalstatus", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[7]>0:
													# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[4]>0:
														# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[5]<=0:
															return 'True'
														elif obj[5]>0:
															return 'False'
														else: return 'False'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[7]<=0:
													return 'False'
												else: return 'False'
											elif obj[14]<=1.0:
												return 'True'
											else: return 'True'
										elif obj[3]>3:
											return 'False'
										else: return 'False'
									elif obj[2]<=0:
										# {"feature": "Weather", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1]<=0:
											return 'False'
										elif obj[1]>0:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]>0:
												return 'True'
											elif obj[5]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[13]>2.0:
									return 'False'
								else: return 'False'
							elif obj[9]<=0:
								# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[2]>2:
									# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[1]<=0:
										# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[13]<=1.0:
											return 'False'
										elif obj[13]>1.0:
											return 'True'
										else: return 'True'
									elif obj[1]>0:
										return 'True'
									else: return 'True'
								elif obj[2]<=2:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[11]<=2:
							return 'False'
						else: return 'False'
					elif obj[10]<=2:
						# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[2]>3:
								return 'True'
							elif obj[2]<=3:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[16]>2:
					# {"feature": "Maritalstatus", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[7]>0:
						# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[11]>0:
							# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[10]<=11:
								return 'False'
							elif obj[10]>11:
								# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]<=1:
									return 'True'
								elif obj[1]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[11]<=0:
							return 'True'
						else: return 'True'
					elif obj[7]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[12]>2.0:
				return 'False'
			else: return 'False'
		elif obj[6]<=1:
			# {"feature": "Income", "instances": 26, "metric_value": 0.8905, "depth": 3}
			if obj[11]<=5:
				# {"feature": "Maritalstatus", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[7]<=1:
					# {"feature": "Children", "instances": 18, "metric_value": 0.8524, "depth": 5}
					if obj[8]>0:
						# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[3]<=3:
								return 'True'
							elif obj[3]>3:
								return 'False'
							else: return 'False'
						elif obj[2]>2:
							return 'False'
						else: return 'False'
					elif obj[8]<=0:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[3]>0:
							return 'True'
						elif obj[3]<=0:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				elif obj[7]>1:
					return 'False'
				else: return 'False'
			elif obj[11]>5:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Occupation", "instances": 43, "metric_value": 0.8204, "depth": 2}
		if obj[10]>1:
			# {"feature": "Weather", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Coupon_validity", "instances": 28, "metric_value": 0.9666, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Time", "instances": 16, "metric_value": 0.8113, "depth": 5}
					if obj[2]>2:
						# {"feature": "Coffeehouse", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[13]>0.0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[6]>0:
								return 'True'
							elif obj[6]<=0:
								return 'False'
							else: return 'False'
						elif obj[13]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				elif obj[4]>0:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[12]<=1.0:
						# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[3]>2:
							# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[14]>0.0:
								return 'True'
							elif obj[14]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=2:
							return 'False'
						else: return 'False'
					elif obj[12]>1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		elif obj[10]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
