def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[15]<=1.0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[10]>2:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]>2:
					return 'True'
				elif obj[3]<=2:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[9]>0:
						return 'False'
					elif obj[9]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[10]<=2:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]>1.0:
		return 'False'
	else: return 'False'
