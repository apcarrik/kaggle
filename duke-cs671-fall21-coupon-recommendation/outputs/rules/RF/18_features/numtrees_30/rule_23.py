def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Coffeehouse", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[13]<=2.0:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 3}
			if obj[10]>2:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[17]<=2:
					# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[2]<=3:
						return 'True'
					elif obj[2]>3:
						# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[15]>1.0:
							return 'False'
						elif obj[15]<=1.0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[17]>2:
					return 'False'
				else: return 'False'
			elif obj[10]<=2:
				return 'True'
			else: return 'True'
		elif obj[13]>2.0:
			# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[10]<=6:
				return 'False'
			elif obj[10]>6:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]>3:
		# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[9]>1:
			return 'False'
		elif obj[9]<=1:
			# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
