def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=14:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9839, "depth": 2}
		if obj[6]<=3:
			# {"feature": "Distance", "instances": 44, "metric_value": 0.9624, "depth": 3}
			if obj[13]<=2:
				# {"feature": "Gender", "instances": 42, "metric_value": 0.9403, "depth": 4}
				if obj[3]>0:
					# {"feature": "Time", "instances": 23, "metric_value": 0.9986, "depth": 5}
					if obj[1]>1:
						# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 6}
						if obj[4]<=3:
							# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[0]<=2:
									# {"feature": "Bar", "instances": 6, "metric_value": 1.0, "depth": 9}
									if obj[9]>0.0:
										# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[8]>0:
											return 'False'
										elif obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[9]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[10]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[4]>3:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 6}
						if obj[11]<=2.0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.7219, "depth": 7}
							if obj[4]>3:
								# {"feature": "Children", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[5]<=0:
									# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 9}
									if obj[2]>3:
										return 'False'
									elif obj[2]<=3:
										# {"feature": "Income", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]>4:
											return 'False'
										elif obj[8]<=4:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[4]<=3:
								return 'False'
							else: return 'False'
						elif obj[11]>2.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=0:
					# {"feature": "Income", "instances": 19, "metric_value": 0.6292, "depth": 5}
					if obj[8]>3:
						return 'True'
					elif obj[8]<=3:
						# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>1:
							# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[0]<=1:
								return 'False'
							elif obj[0]>1:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>2:
									return 'True'
								elif obj[4]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[13]>2:
				return 'False'
			else: return 'False'
		elif obj[6]>3:
			return 'False'
		else: return 'False'
	elif obj[7]>14:
		return 'False'
	else: return 'False'
