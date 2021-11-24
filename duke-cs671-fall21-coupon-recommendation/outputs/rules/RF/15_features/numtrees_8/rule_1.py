def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Time", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 64, "metric_value": 0.896, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 51, "metric_value": 0.7871, "depth": 3}
			if obj[8]<=14.983825694278288:
				# {"feature": "Age", "instances": 42, "metric_value": 0.65, "depth": 4}
				if obj[5]<=5:
					# {"feature": "Income", "instances": 34, "metric_value": 0.7335, "depth": 5}
					if obj[9]>0:
						# {"feature": "Bar", "instances": 27, "metric_value": 0.8256, "depth": 6}
						if obj[10]>0.0:
							# {"feature": "Coupon_validity", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[3]>0:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[0]>0:
									# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 9}
									if obj[4]<=0:
										return 'False'
									elif obj[4]>0:
										# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[7]<=0:
											return 'True'
										elif obj[7]>0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 8}
								if obj[11]>2.0:
									return 'True'
								elif obj[11]<=2.0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>1:
										return 'True'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[10]<=0.0:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.4395, "depth": 7}
							if obj[11]<=2.0:
								return 'True'
							elif obj[11]>2.0:
								# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>0:
									return 'True'
								elif obj[3]<=0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>5:
					return 'True'
				else: return 'True'
			elif obj[8]>14.983825694278288:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0:
								return 'True'
							elif obj[4]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]<=0.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Age", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[5]>1:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[12]>0.0:
						return 'False'
					elif obj[12]<=0.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Passanger", "instances": 63, "metric_value": 0.9911, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 61, "metric_value": 0.9842, "depth": 3}
			if obj[8]>0:
				# {"feature": "Age", "instances": 59, "metric_value": 0.9748, "depth": 4}
				if obj[5]<=4:
					# {"feature": "Coupon", "instances": 46, "metric_value": 0.9945, "depth": 5}
					if obj[2]<=3:
						# {"feature": "Income", "instances": 32, "metric_value": 0.9887, "depth": 6}
						if obj[9]>0:
							# {"feature": "Coffeehouse", "instances": 28, "metric_value": 1.0, "depth": 7}
							if obj[11]>0.0:
								# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9877, "depth": 8}
								if obj[13]<=0:
									# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 9}
									if obj[7]<=3:
										# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9957, "depth": 10}
										if obj[3]<=0:
											# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 11}
											if obj[10]<=1.0:
												# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[12]>0.0:
													# {"feature": "Gender", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[4]>0:
														# {"feature": "Children", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[6]>0:
															# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[14]>1:
																return 'False'
															elif obj[14]<=1:
																return 'True'
															else: return 'True'
														elif obj[6]<=0:
															return 'False'
														else: return 'False'
													elif obj[4]<=0:
														return 'True'
													else: return 'True'
												elif obj[12]<=0.0:
													return 'False'
												else: return 'False'
											elif obj[10]>1.0:
												return 'False'
											else: return 'False'
										elif obj[3]>0:
											# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[12]<=1.0:
												return 'True'
											elif obj[12]>1.0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[7]>3:
										return 'True'
									else: return 'True'
								elif obj[13]>0:
									# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[14]>1:
											return 'False'
										elif obj[14]<=1:
											return 'True'
										else: return 'True'
									else: return 'False'
								else: return 'False'
							elif obj[11]<=0.0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[14]<=1:
									return 'True'
								elif obj[14]>1:
									# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[3]>0:
										return 'True'
									elif obj[3]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'True'
						elif obj[9]<=0:
							return 'True'
						else: return 'True'
					elif obj[2]>3:
						# {"feature": "Distance", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[14]<=2:
							# {"feature": "Bar", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[10]>1.0:
								# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[12]>0.0:
									# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[4]>0:
										return 'False'
									elif obj[4]<=0:
										# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]<=1:
											return 'True'
										elif obj[7]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[12]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[10]<=1.0:
								return 'False'
							else: return 'False'
						elif obj[14]>2:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[5]>4:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 5}
					if obj[2]<=3:
						return 'False'
					elif obj[2]>3:
						# {"feature": "Income", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[9]>2:
							return 'True'
						elif obj[9]<=2:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[8]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
