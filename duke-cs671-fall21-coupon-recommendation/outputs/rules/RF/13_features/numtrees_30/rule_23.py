def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Passanger", "instances": 29, "metric_value": 0.9991, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 19, "metric_value": 0.998, "depth": 4}
				if obj[12]<=2:
					# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Gender", "instances": 12, "metric_value": 1.0, "depth": 6}
						if obj[3]>0:
							# {"feature": "Coffeehouse", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[9]>0.0:
								# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									# {"feature": "Children", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=0:
										return 'False'
									elif obj[5]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[9]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[3]<=0:
							# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]>2:
								return 'True'
							elif obj[4]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[12]>2:
					return 'True'
				else: return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[2]<=3:
				return 'True'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
