def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Coffeehouse", "instances": 117, "metric_value": 0.9974, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Distance", "instances": 82, "metric_value": 0.9961, "depth": 3}
			if obj[13]<=2:
				# {"feature": "Time", "instances": 73, "metric_value": 0.977, "depth": 4}
				if obj[1]>0:
					# {"feature": "Income", "instances": 58, "metric_value": 0.9294, "depth": 5}
					if obj[8]<=6:
						# {"feature": "Direction_same", "instances": 51, "metric_value": 0.9662, "depth": 6}
						if obj[12]<=0:
							# {"feature": "Occupation", "instances": 43, "metric_value": 0.9103, "depth": 7}
							if obj[7]>1:
								# {"feature": "Bar", "instances": 39, "metric_value": 0.8582, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Coupon", "instances": 38, "metric_value": 0.8315, "depth": 9}
									if obj[2]>0:
										# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.7455, "depth": 10}
										if obj[11]>-1.0:
											# {"feature": "Age", "instances": 32, "metric_value": 0.6962, "depth": 11}
											if obj[4]<=4:
												# {"feature": "Children", "instances": 26, "metric_value": 0.7793, "depth": 12}
												if obj[5]>0:
													# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 13}
													if obj[0]>2:
														# {"feature": "Gender", "instances": 8, "metric_value": 0.8113, "depth": 14}
														if obj[3]>0:
															return 'True'
														elif obj[3]<=0:
															return 'True'
														else: return 'True'
													elif obj[0]<=2:
														return 'True'
													else: return 'True'
												elif obj[5]<=0:
													# {"feature": "Passanger", "instances": 12, "metric_value": 0.9183, "depth": 13}
													if obj[0]<=1:
														# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 14}
														if obj[3]<=0:
															return 'True'
														elif obj[3]>0:
															return 'False'
														else: return 'False'
													elif obj[0]>1:
														# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 14}
														if obj[3]<=0:
															return 'True'
														elif obj[3]>0:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											elif obj[4]>4:
												return 'True'
											else: return 'True'
										elif obj[11]<=-1.0:
											return 'False'
										else: return 'False'
									elif obj[2]<=0:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[0]<=1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]>1.0:
													return 'True'
												elif obj[11]<=1.0:
													return 'False'
												else: return 'False'
											elif obj[3]>0:
												return 'True'
											else: return 'True'
										elif obj[0]>1:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=-1.0:
									return 'False'
								else: return 'False'
							elif obj[7]<=1:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>2:
									# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=3:
										return 'False'
									elif obj[4]>3:
										return 'True'
									else: return 'True'
								elif obj[0]<=2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[12]>0:
							# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[4]<=2:
								return 'False'
							elif obj[4]>2:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]<=0.0:
									# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]<=1:
										# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[2]<=3:
											# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[5]<=0:
													# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[7]<=7:
														# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 14}
														if obj[9]<=2.0:
															return 'True'
														else: return 'True'
													else: return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[11]>0.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[8]>6:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[7]<=9:
						# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[2]>1:
							# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[0]<=1:
								return 'True'
							elif obj[0]>1:
								# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'True'
								elif obj[3]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[7]>9:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[13]>2:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'False'
		elif obj[10]<=0.0:
			# {"feature": "Bar", "instances": 35, "metric_value": 0.8981, "depth": 3}
			if obj[9]<=0.0:
				# {"feature": "Coupon", "instances": 25, "metric_value": 0.971, "depth": 4}
				if obj[2]>2:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[11]<=1.0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[7]<=12:
							# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[3]>0:
								# {"feature": "Children", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[5]>0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]>1:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[13]>1:
											return 'True'
										elif obj[13]<=1:
											return 'False'
										else: return 'False'
									elif obj[0]<=1:
										return 'False'
									else: return 'False'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]>12:
							return 'True'
						else: return 'True'
					elif obj[11]>1.0:
						return 'True'
					else: return 'True'
				elif obj[2]<=2:
					# {"feature": "Income", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[8]>1:
						return 'False'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[9]>0.0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[11]>0.0:
					return 'False'
				elif obj[11]<=0.0:
					# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						return 'False'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[6]>3:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[7]>1:
			return 'True'
		elif obj[7]<=1:
			return 'False'
		else: return 'False'
	else: return 'True'
