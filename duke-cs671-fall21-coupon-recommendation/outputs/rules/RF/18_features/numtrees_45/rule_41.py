def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[6]<=4:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[13]>0.0:
			# {"feature": "Restaurantlessthan20", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[14]>1.0:
				# {"feature": "Direction_same", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[16]<=0:
					return 'True'
				elif obj[16]>0:
					return 'False'
				else: return 'False'
			elif obj[14]<=1.0:
				return 'False'
			else: return 'False'
		elif obj[13]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[6]>4:
		return 'True'
	else: return 'True'
