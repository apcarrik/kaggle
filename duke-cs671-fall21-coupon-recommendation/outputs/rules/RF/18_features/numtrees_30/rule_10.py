def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurantlessthan20, obj[15]: Restaurant20to50, obj[16]: Direction_same, obj[17]: Distance
	# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.6098, "depth": 2}
		if obj[10]>6:
			return 'True'
		elif obj[10]<=6:
			# {"feature": "Gender", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[5]<=0:
				# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[6]>1:
					return 'False'
				elif obj[6]<=1:
					return 'True'
				else: return 'True'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>0:
		# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[15]<=1.0:
			return 'False'
		elif obj[15]>1.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
