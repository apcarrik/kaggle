def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[6]<=3:
		# {"feature": "Income", "instances": 22, "metric_value": 1.0, "depth": 2}
		if obj[11]<=5:
			# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 4}
				if obj[10]>2:
					# {"feature": "Passanger", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[17]<=1:
							# {"feature": "Coupon", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[3]>2:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[12]>0.0:
									return 'False'
								elif obj[12]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[3]<=2:
								return 'True'
							else: return 'True'
						elif obj[17]>1:
							return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[10]<=2:
					return 'False'
				else: return 'False'
			elif obj[13]<=0.0:
				return 'True'
			else: return 'True'
		elif obj[11]>5:
			return 'True'
		else: return 'True'
	elif obj[6]>3:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[3]<=3:
			return 'True'
		elif obj[3]>3:
			# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]>0:
				return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
