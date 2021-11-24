def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Passanger", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Restaurant20to50", "instances": 74, "metric_value": 0.9979, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Coffeehouse", "instances": 71, "metric_value": 0.993, "depth": 3}
			if obj[7]<=3.0:
				# {"feature": "Age", "instances": 67, "metric_value": 0.9986, "depth": 4}
				if obj[3]<=6:
					# {"feature": "Occupation", "instances": 61, "metric_value": 0.9998, "depth": 5}
					if obj[5]<=17:
						# {"feature": "Bar", "instances": 59, "metric_value": 0.9998, "depth": 6}
						if obj[6]<=1.0:
							# {"feature": "Education", "instances": 46, "metric_value": 0.9945, "depth": 7}
							if obj[4]<=1:
								# {"feature": "Direction_same", "instances": 24, "metric_value": 0.9544, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 9}
									if obj[2]>1:
										# {"feature": "Time", "instances": 13, "metric_value": 0.9612, "depth": 10}
										if obj[1]<=3:
											# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 11}
											if obj[10]>1:
												return 'True'
											elif obj[10]<=1:
												return 'True'
											else: return 'True'
										elif obj[1]>3:
											return 'True'
										else: return 'True'
									elif obj[2]<=1:
										# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[10]<=2:
											return 'False'
										elif obj[10]>2:
											# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[1]>0:
												return 'True'
											elif obj[1]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									else: return 'False'
								elif obj[9]>0:
									return 'True'
								else: return 'True'
							elif obj[4]>1:
								# {"feature": "Coupon", "instances": 22, "metric_value": 0.994, "depth": 8}
								if obj[2]>3:
									# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 9}
									if obj[10]>1:
										# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 10}
										if obj[1]<=1:
											return 'False'
										elif obj[1]>1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[10]<=1:
										# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[1]<=0:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]<=0:
												return 'False'
											else: return 'False'
										elif obj[1]>0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=1:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[2]<=3:
									# {"feature": "Time", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[1]>0:
										# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[10]<=1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.7219, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'True'
											else: return 'True'
										elif obj[10]>1:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[9]<=0:
												return 'True'
											elif obj[9]>0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[1]<=0:
										return 'False'
									else: return 'False'
								else: return 'True'
							else: return 'False'
						elif obj[6]>1.0:
							# {"feature": "Education", "instances": 13, "metric_value": 0.8905, "depth": 7}
							if obj[4]>0:
								# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 8}
								if obj[1]>0:
									# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[2]<=3:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[10]>1:
											# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[10]<=1:
											return 'True'
										else: return 'True'
									elif obj[2]>3:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]>17:
						return 'True'
					else: return 'True'
				elif obj[3]>6:
					# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[9]<=0:
						return 'False'
					elif obj[9]>0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]>3.0:
				return 'False'
			else: return 'False'
		elif obj[8]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>1:
		# {"feature": "Age", "instances": 53, "metric_value": 0.7717, "depth": 2}
		if obj[3]<=3:
			# {"feature": "Occupation", "instances": 29, "metric_value": 0.9784, "depth": 3}
			if obj[5]<=20:
				# {"feature": "Education", "instances": 26, "metric_value": 0.9306, "depth": 4}
				if obj[4]>1:
					# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 5}
					if obj[2]>0:
						# {"feature": "Time", "instances": 13, "metric_value": 0.6194, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Restaurant20to50", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[8]<=1.0:
								# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Bar", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'False'
											else: return 'False'
										else: return 'False'
									elif obj[6]<=0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=0:
											# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=2:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[8]>1.0:
								return 'True'
							else: return 'True'
						elif obj[1]>2:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[10]<=1:
								# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[2]>2:
									# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>0.0:
											return 'False'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[6]>0.0:
										return 'True'
									else: return 'True'
								elif obj[2]<=2:
									return 'False'
								else: return 'False'
							elif obj[10]>1:
								return 'False'
							else: return 'False'
						elif obj[8]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[1]>2:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>0.0:
							return 'True'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[5]>20:
				return 'False'
			else: return 'False'
		elif obj[3]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
