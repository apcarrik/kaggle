def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Bar", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[7]<=2.0:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[2]>1:
			# {"feature": "Distance", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[11]<=2:
				# {"feature": "Education", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[5]<=3:
					# {"feature": "Age", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[4]>0:
						# {"feature": "Direction_same", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[10]<=0:
							# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 7}
							if obj[8]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 8}
								if obj[9]<=1.0:
									# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 9}
									if obj[6]<=7:
										# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 10}
										if obj[1]<=2:
											return 'True'
										elif obj[1]>2:
											return 'False'
										else: return 'False'
									elif obj[6]>7:
										# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[1]<=2:
											return 'False'
										elif obj[1]>2:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[9]>1.0:
									return 'True'
								else: return 'True'
							elif obj[8]>2.0:
								return 'False'
							else: return 'False'
						elif obj[10]>0:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[5]>3:
					return 'False'
				else: return 'False'
			elif obj[11]>2:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[7]>2.0:
		# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[2]<=3:
			return 'True'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	else: return 'True'
