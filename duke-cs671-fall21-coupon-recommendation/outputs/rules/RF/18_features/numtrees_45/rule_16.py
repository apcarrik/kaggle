def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[10]>4:
		# {"feature": "Bar", "instances": 19, "metric_value": 0.7425, "depth": 2}
		if obj[12]<=0.0:
			# {"feature": "Coffeehouse", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[13]>0.0:
				# {"feature": "Restaurantlessthan20", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[14]<=2.0:
					return 'True'
				elif obj[14]>2.0:
					return 'False'
				else: return 'False'
			elif obj[13]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[12]>0.0:
			return 'False'
		else: return 'False'
	elif obj[10]<=4:
		return 'True'
	else: return 'True'
