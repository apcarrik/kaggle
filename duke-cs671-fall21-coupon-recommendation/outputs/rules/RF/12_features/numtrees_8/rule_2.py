def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 127, "metric_value": 0.9924, "depth": 1}
	if obj[6]<=8.598425196850394:
		# {"feature": "Bar", "instances": 73, "metric_value": 0.9395, "depth": 2}
		if obj[7]<=2.0:
			# {"feature": "Age", "instances": 69, "metric_value": 0.9558, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Restaurant20to50", "instances": 36, "metric_value": 0.9978, "depth": 4}
				if obj[9]<=2.0:
					# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 5}
					if obj[11]>1:
						# {"feature": "Direction_same", "instances": 25, "metric_value": 0.9988, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Coffeehouse", "instances": 22, "metric_value": 0.994, "depth": 7}
							if obj[8]<=3.0:
								# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 8}
								if obj[5]>0:
									# {"feature": "Time", "instances": 16, "metric_value": 0.896, "depth": 9}
									if obj[1]<=3:
										# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 10}
										if obj[0]>1:
											# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 11}
											if obj[2]>3:
												# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[3]>0:
													return 'False'
												elif obj[3]<=0:
													return 'True'
												else: return 'True'
											elif obj[2]<=3:
												return 'True'
											else: return 'True'
										elif obj[0]<=1:
											# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 11}
											if obj[2]>0:
												# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[3]<=0:
													return 'False'
												elif obj[3]>0:
													return 'False'
												else: return 'False'
											elif obj[2]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[1]>3:
										return 'True'
									else: return 'True'
								elif obj[5]<=0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]>0:
										return 'False'
									elif obj[0]<=0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[8]>3.0:
								return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'False'
						else: return 'False'
					elif obj[11]<=1:
						# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=0:
								return 'False'
							elif obj[1]>0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[9]>2.0:
					return 'False'
				else: return 'False'
			elif obj[4]>3:
				# {"feature": "Education", "instances": 33, "metric_value": 0.8454, "depth": 4}
				if obj[5]<=1:
					# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.5226, "depth": 5}
					if obj[8]<=3.0:
						# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.3373, "depth": 6}
						if obj[9]>0.0:
							return 'True'
						elif obj[9]<=0.0:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]>0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[10]<=0:
									return 'True'
								elif obj[10]>0:
									return 'False'
								else: return 'False'
							elif obj[1]<=0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>3.0:
						return 'False'
					else: return 'False'
				elif obj[5]>1:
					# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9887, "depth": 5}
					if obj[9]<=1.0:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Direction_same", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[10]<=0:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[8]<=2.0:
									# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[2]<=2:
										return 'True'
									elif obj[2]>2:
										# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[3]>0:
											return 'True'
										elif obj[3]<=0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[8]>2.0:
									return 'False'
								else: return 'False'
							elif obj[10]>0:
								return 'False'
							else: return 'False'
						elif obj[0]>2:
							return 'False'
						else: return 'False'
					elif obj[9]>1.0:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]>0:
							return 'True'
						elif obj[1]<=0:
							# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>1:
								return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]>2.0:
			return 'True'
		else: return 'True'
	elif obj[6]>8.598425196850394:
		# {"feature": "Coffeehouse", "instances": 54, "metric_value": 0.9841, "depth": 2}
		if obj[8]<=3.0:
			# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9662, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Direction_same", "instances": 37, "metric_value": 0.9995, "depth": 4}
				if obj[10]<=0:
					# {"feature": "Coupon", "instances": 31, "metric_value": 0.9812, "depth": 5}
					if obj[2]>0:
						# {"feature": "Bar", "instances": 27, "metric_value": 0.999, "depth": 6}
						if obj[7]>0.0:
							# {"feature": "Time", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[1]>0:
								# {"feature": "Passanger", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[0]>1:
									return 'False'
								elif obj[0]<=1:
									# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[4]>2:
										return 'False'
									elif obj[4]<=2:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]<=0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[5]>0:
									# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[0]<=1:
										return 'False'
									elif obj[0]>1:
										# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[4]<=1:
											return 'True'
										elif obj[4]>1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[5]<=0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[7]<=0.0:
							# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[5]>0:
								# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[1]<=2:
									# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[4]>0:
										# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[0]>1:
											# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[3]>0:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=2:
													return 'False'
												else: return 'False'
											elif obj[3]<=0:
												return 'True'
											else: return 'True'
										elif obj[0]<=1:
											return 'True'
										else: return 'True'
									elif obj[4]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]>2:
									return 'True'
								else: return 'True'
							elif obj[5]<=0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[10]>0:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>0:
						return 'True'
					elif obj[1]<=0:
						# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[9]>1.0:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.5917, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>1:
							return 'True'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[8]>3.0:
			return 'True'
		else: return 'True'
	else: return 'False'
