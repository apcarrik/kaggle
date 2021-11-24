def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[11]<=6:
		# {"feature": "Coupon_validity", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[4]<=0:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[10]<=10:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[17]<=2:
					# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[9]>1:
						# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[6]>0:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]<=0:
								# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]>1:
									return 'False'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							elif obj[2]>0:
								return 'False'
							else: return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					elif obj[9]<=1:
						return 'True'
					else: return 'True'
				elif obj[17]>2:
					return 'False'
				else: return 'False'
			elif obj[10]>10:
				return 'True'
			else: return 'True'
		elif obj[4]>0:
			# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]>1:
					return 'True'
				elif obj[6]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[11]>6:
		return 'True'
	else: return 'True'
