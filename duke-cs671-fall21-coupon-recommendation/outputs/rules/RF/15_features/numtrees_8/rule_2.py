def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Bar", "instances": 75, "metric_value": 0.971, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.8673, "depth": 3}
			if obj[2]>0:
				# {"feature": "Occupation", "instances": 36, "metric_value": 0.9436, "depth": 4}
				if obj[8]<=14:
					# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9812, "depth": 5}
					if obj[11]<=2.0:
						# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 6}
						if obj[7]>0:
							# {"feature": "Time", "instances": 17, "metric_value": 0.9367, "depth": 7}
							if obj[1]>0:
								# {"feature": "Age", "instances": 12, "metric_value": 1.0, "depth": 8}
								if obj[5]<=4:
									# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 9}
									if obj[12]>0.0:
										# {"feature": "Income", "instances": 8, "metric_value": 1.0, "depth": 10}
										if obj[9]>0:
											# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 11}
											if obj[13]<=0:
												# {"feature": "Coupon_validity", "instances": 6, "metric_value": 1.0, "depth": 12}
												if obj[3]<=0:
													# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[14]>1:
														# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[4]>0:
															# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 15}
															if obj[6]<=0:
																return 'True'
															elif obj[6]>0:
																return 'False'
															else: return 'False'
														elif obj[4]<=0:
															return 'True'
														else: return 'True'
													elif obj[14]<=1:
														return 'False'
													else: return 'False'
												elif obj[3]>0:
													return 'True'
												else: return 'True'
											elif obj[13]>0:
												return 'False'
											else: return 'False'
										elif obj[9]<=0:
											return 'True'
										else: return 'True'
									elif obj[12]<=0.0:
										return 'False'
									else: return 'False'
								elif obj[5]>4:
									return 'True'
								else: return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						elif obj[7]<=0:
							# {"feature": "Coupon_validity", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[3]>0:
								# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[14]<=1:
									return 'True'
								elif obj[14]>1:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]>2.0:
						return 'False'
					else: return 'False'
				elif obj[8]>14:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[10]>1.0:
			# {"feature": "Age", "instances": 30, "metric_value": 0.9871, "depth": 3}
			if obj[5]>0:
				# {"feature": "Income", "instances": 27, "metric_value": 0.951, "depth": 4}
				if obj[9]<=4:
					# {"feature": "Occupation", "instances": 21, "metric_value": 0.9984, "depth": 5}
					if obj[8]>1:
						# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9911, "depth": 6}
						if obj[12]>0.0:
							# {"feature": "Distance", "instances": 16, "metric_value": 1.0, "depth": 7}
							if obj[14]<=2:
								# {"feature": "Time", "instances": 14, "metric_value": 0.9852, "depth": 8}
								if obj[1]>0:
									# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 9}
									if obj[7]<=3:
										# {"feature": "Children", "instances": 9, "metric_value": 0.7642, "depth": 10}
										if obj[6]<=0:
											# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[4]<=0:
												# {"feature": "Coupon_validity", "instances": 6, "metric_value": 0.65, "depth": 12}
												if obj[3]<=0:
													return 'True'
												elif obj[3]>0:
													# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[11]>2.0:
														return 'False'
													elif obj[11]<=2.0:
														return 'True'
													else: return 'True'
												else: return 'False'
											elif obj[4]>0:
												return 'False'
											else: return 'False'
										elif obj[6]>0:
											return 'True'
										else: return 'True'
									elif obj[7]>3:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[2]>3:
										return 'False'
									elif obj[2]<=3:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[14]>2:
								return 'False'
							else: return 'False'
						elif obj[12]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				elif obj[9]>4:
					return 'True'
				else: return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Coupon", "instances": 52, "metric_value": 0.8667, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon_validity", "instances": 38, "metric_value": 0.6892, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Income", "instances": 20, "metric_value": 0.2864, "depth": 4}
				if obj[9]>1:
					return 'True'
				elif obj[9]<=1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5]<=3:
						return 'True'
					elif obj[5]>3:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>0:
				# {"feature": "Age", "instances": 18, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=4:
					# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[8]<=7:
						# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[9]<=5:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[11]<=2.0:
								return 'False'
							elif obj[11]>2.0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>2:
									return 'False'
								elif obj[1]<=2:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[9]>5:
							return 'True'
						else: return 'True'
					elif obj[8]>7:
						# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[11]>0.0:
							return 'True'
						elif obj[11]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>4:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[10]>0.0:
				# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]>3:
					return 'True'
				elif obj[5]<=3:
					# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]>2:
						return 'False'
					elif obj[9]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[10]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
