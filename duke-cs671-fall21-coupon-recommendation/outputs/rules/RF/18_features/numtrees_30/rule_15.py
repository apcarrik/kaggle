def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[17]>1:
		# {"feature": "Education", "instances": 22, "metric_value": 1.0, "depth": 2}
		if obj[9]<=3:
			# {"feature": "Passanger", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[3]>1:
					# {"feature": "Restaurantlessthan20", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[14]>1.0:
						# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[2]<=3:
							return 'True'
						elif obj[2]>3:
							# {"feature": "Coupon_validity", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>0:
								return 'False'
							elif obj[4]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[14]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[9]>3:
			return 'False'
		else: return 'False'
	elif obj[17]<=1:
		# {"feature": "Age", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[6]>0:
			return 'True'
		elif obj[6]<=0:
			# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=0:
				return 'True'
			elif obj[0]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
