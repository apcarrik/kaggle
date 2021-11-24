def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[13]>1:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[10]<=2.0:
			# {"feature": "Direction_same", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[12]<=0:
				# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 6}
						if obj[7]>6:
							# {"feature": "Income", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[8]<=6:
								# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[0]<=2:
									return 'False'
								elif obj[0]>2:
									# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[1]<=2:
										return 'True'
									elif obj[1]>2:
										return 'False'
									else: return 'False'
								else: return 'True'
							elif obj[8]>6:
								return 'True'
							else: return 'True'
						elif obj[7]<=6:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[12]>0:
				return 'True'
			else: return 'True'
		elif obj[10]>2.0:
			return 'True'
		else: return 'True'
	elif obj[13]<=1:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[7]<=11:
			return 'True'
		elif obj[7]>11:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
