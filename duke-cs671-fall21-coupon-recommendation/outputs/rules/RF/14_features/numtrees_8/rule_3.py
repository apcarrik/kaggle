def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Children", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Age", "instances": 82, "metric_value": 0.965, "depth": 2}
		if obj[4]>0:
			# {"feature": "Gender", "instances": 74, "metric_value": 0.9868, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Passanger", "instances": 46, "metric_value": 0.9945, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9294, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 6}
						if obj[6]>1:
							# {"feature": "Bar", "instances": 14, "metric_value": 0.8631, "depth": 7}
							if obj[9]<=2.0:
								# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[8]<=6:
									return 'False'
								elif obj[8]>6:
									return 'True'
								else: return 'True'
							elif obj[9]>2.0:
								# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[1]<=2:
									return 'True'
								elif obj[1]>2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[6]<=1:
							# {"feature": "Income", "instances": 9, "metric_value": 0.9183, "depth": 7}
							if obj[8]>2:
								# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[7]>4:
									# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[2]>0:
										return 'True'
									elif obj[2]<=0:
										return 'False'
									else: return 'False'
								elif obj[7]<=4:
									return 'False'
								else: return 'False'
							elif obj[8]<=2:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[11]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[0]>1:
					# {"feature": "Occupation", "instances": 17, "metric_value": 0.9367, "depth": 5}
					if obj[7]<=7:
						# {"feature": "Income", "instances": 15, "metric_value": 0.8366, "depth": 6}
						if obj[8]<=7:
							# {"feature": "Time", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[11]>0.0:
									return 'False'
								elif obj[11]<=0.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>7:
							return 'False'
						else: return 'False'
					elif obj[7]>7:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[3]>0:
				# {"feature": "Education", "instances": 28, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=3:
					# {"feature": "Distance", "instances": 24, "metric_value": 0.65, "depth": 5}
					if obj[13]<=1:
						return 'True'
					elif obj[13]>1:
						# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[1]>1:
							# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[2]>2:
								# {"feature": "Income", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[8]<=4:
									return 'False'
								elif obj[8]>4:
									return 'True'
								else: return 'True'
							elif obj[2]<=2:
								return 'True'
							else: return 'True'
						elif obj[1]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[6]>3:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]<=0:
						return 'False'
					elif obj[2]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'True'
		elif obj[4]<=0:
			return 'True'
		else: return 'True'
	elif obj[5]>0:
		# {"feature": "Coupon", "instances": 45, "metric_value": 0.9565, "depth": 2}
		if obj[2]>0:
			# {"feature": "Occupation", "instances": 39, "metric_value": 0.9881, "depth": 3}
			if obj[7]>1:
				# {"feature": "Coffeehouse", "instances": 34, "metric_value": 1.0, "depth": 4}
				if obj[10]<=3.0:
					# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.9784, "depth": 5}
					if obj[11]>0.0:
						# {"feature": "Direction_same", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[12]<=0:
							# {"feature": "Age", "instances": 22, "metric_value": 0.994, "depth": 7}
							if obj[4]>0:
								# {"feature": "Bar", "instances": 19, "metric_value": 0.998, "depth": 8}
								if obj[9]>-1.0:
									# {"feature": "Time", "instances": 17, "metric_value": 0.9975, "depth": 9}
									if obj[1]>1:
										# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 10}
										if obj[13]>1:
											# {"feature": "Income", "instances": 11, "metric_value": 0.9457, "depth": 11}
											if obj[8]<=4:
												# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 12}
												if obj[6]>1:
													# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 13}
													if obj[0]<=2:
														# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 14}
														if obj[3]<=0:
															return 'True'
														elif obj[3]>0:
															return 'False'
														else: return 'False'
													elif obj[0]>2:
														return 'True'
													else: return 'True'
												elif obj[6]<=1:
													return 'True'
												else: return 'True'
											elif obj[8]>4:
												# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[0]>2:
													# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[6]<=0:
														return 'False'
													elif obj[6]>0:
														return 'True'
													else: return 'True'
												elif obj[0]<=2:
													return 'False'
												else: return 'False'
											else: return 'False'
										elif obj[13]<=1:
											return 'False'
										else: return 'False'
									elif obj[1]<=1:
										# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[0]<=1:
											return 'False'
										elif obj[0]>1:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]<=-1.0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						elif obj[12]>0:
							return 'True'
						else: return 'True'
					elif obj[11]<=0.0:
						return 'True'
					else: return 'True'
				elif obj[10]>3.0:
					return 'False'
				else: return 'False'
			elif obj[7]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
