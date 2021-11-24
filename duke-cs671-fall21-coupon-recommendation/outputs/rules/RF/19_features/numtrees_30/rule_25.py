def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[4]>1:
		# {"feature": "Restaurantlessthan20", "instances": 26, "metric_value": 1.0, "depth": 2}
		if obj[15]>2.0:
			# {"feature": "Gender", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[6]>0:
				return 'False'
			elif obj[6]<=0:
				# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[18]<=1:
					return 'True'
				elif obj[18]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[15]<=2.0:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[10]<=2:
				return 'True'
			elif obj[10]>2:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[7]>2:
					return 'False'
				elif obj[7]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[4]<=1:
		return 'False'
	else: return 'False'
