def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[5]<=1:
		# {"feature": "Age", "instances": 44, "metric_value": 0.9024, "depth": 2}
		if obj[4]<=6:
			# {"feature": "Distance", "instances": 42, "metric_value": 0.8631, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Occupation", "instances": 35, "metric_value": 0.7755, "depth": 4}
				if obj[6]<=12:
					# {"feature": "Bar", "instances": 28, "metric_value": 0.5917, "depth": 5}
					if obj[7]>0.0:
						return 'True'
					elif obj[7]<=0.0:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[0]<=2:
							# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[2]>2:
									# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[3]<=0:
										return 'True'
									elif obj[3]>0:
										# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]>1.0:
											return 'True'
										elif obj[8]<=1.0:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[2]<=2:
									return 'False'
								else: return 'False'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						elif obj[0]>2:
							# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[1]>2:
								return 'False'
							elif obj[1]<=2:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[6]>12:
					# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]>2:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2]>2:
						# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=0:
							return 'False'
						elif obj[3]>0:
							return 'True'
						else: return 'True'
					elif obj[2]<=2:
						return 'True'
					else: return 'True'
				elif obj[9]>1.0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[4]>6:
			return 'False'
		else: return 'False'
	elif obj[5]>1:
		# {"feature": "Restaurant20to50", "instances": 41, "metric_value": 0.9789, "depth": 2}
		if obj[9]<=2.0:
			# {"feature": "Occupation", "instances": 38, "metric_value": 0.9495, "depth": 3}
			if obj[6]>2:
				# {"feature": "Passanger", "instances": 33, "metric_value": 0.9834, "depth": 4}
				if obj[0]>0:
					# {"feature": "Coffeehouse", "instances": 31, "metric_value": 0.9629, "depth": 5}
					if obj[8]>-1.0:
						# {"feature": "Coupon", "instances": 29, "metric_value": 0.9294, "depth": 6}
						if obj[2]>0:
							# {"feature": "Bar", "instances": 23, "metric_value": 0.8281, "depth": 7}
							if obj[7]<=2.0:
								# {"feature": "Gender", "instances": 20, "metric_value": 0.8813, "depth": 8}
								if obj[3]>0:
									# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 9}
									if obj[1]<=2:
										# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[11]<=2:
											# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Age", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[4]<=0:
													return 'False'
												elif obj[4]>0:
													return 'True'
												else: return 'True'
											elif obj[10]>0:
												return 'False'
											else: return 'False'
										elif obj[11]>2:
											return 'False'
										else: return 'False'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								elif obj[3]<=0:
									# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 9}
									if obj[4]>1:
										# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[1]>1:
											return 'False'
										elif obj[1]<=1:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[10]<=0:
												# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[11]<=1:
													return 'True'
												else: return 'True'
											else: return 'True'
										else: return 'True'
									elif obj[4]<=1:
										# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[1]>1:
											return 'True'
										elif obj[1]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								else: return 'False'
							elif obj[7]>2.0:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0:
								return 'True'
							elif obj[4]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]<=2:
				return 'False'
			else: return 'False'
		elif obj[9]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
