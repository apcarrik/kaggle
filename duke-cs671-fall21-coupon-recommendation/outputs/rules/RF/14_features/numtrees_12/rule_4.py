def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]>0:
		# {"feature": "Passanger", "instances": 73, "metric_value": 0.9934, "depth": 2}
		if obj[0]>0:
			# {"feature": "Children", "instances": 70, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Bar", "instances": 37, "metric_value": 0.9953, "depth": 4}
				if obj[9]<=1.0:
					# {"feature": "Income", "instances": 19, "metric_value": 0.9495, "depth": 5}
					if obj[8]>3:
						# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 6}
						if obj[7]>5:
							# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[13]<=2:
								# {"feature": "Gender", "instances": 9, "metric_value": 0.7642, "depth": 8}
								if obj[3]<=0:
									# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[6]<=0:
										return 'True'
									elif obj[6]>0:
										return 'False'
									else: return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							elif obj[13]>2:
								return 'False'
							else: return 'False'
						elif obj[7]<=5:
							return 'False'
						else: return 'False'
					elif obj[8]<=3:
						return 'True'
					else: return 'True'
				elif obj[9]>1.0:
					# {"feature": "Occupation", "instances": 18, "metric_value": 0.8524, "depth": 5}
					if obj[7]>1:
						# {"feature": "Time", "instances": 15, "metric_value": 0.5665, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[13]<=1:
								return 'True'
							elif obj[13]>1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[7]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>0:
				# {"feature": "Age", "instances": 33, "metric_value": 0.885, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 25, "metric_value": 0.971, "depth": 5}
					if obj[6]>0:
						# {"feature": "Occupation", "instances": 18, "metric_value": 0.9911, "depth": 6}
						if obj[7]<=14:
							# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 7}
							if obj[9]>-1.0:
								# {"feature": "Coffeehouse", "instances": 15, "metric_value": 0.9183, "depth": 8}
								if obj[10]>1.0:
									# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.994, "depth": 9}
									if obj[11]<=1.0:
										# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 10}
										if obj[3]>0:
											return 'False'
										elif obj[3]<=0:
											# {"feature": "Income", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]>0:
												return 'True'
											elif obj[8]<=0:
												return 'False'
											else: return 'False'
										else: return 'True'
									elif obj[11]>1.0:
										# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]<=2:
											return 'True'
										elif obj[8]>2:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[10]<=1.0:
									return 'False'
								else: return 'False'
							elif obj[9]<=-1.0:
								return 'True'
							else: return 'True'
						elif obj[7]>14:
							return 'True'
						else: return 'True'
					elif obj[6]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=0:
		# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[6]<=2:
			return 'False'
		elif obj[6]>2:
			# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[7]>6:
				return 'True'
			elif obj[7]<=6:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
