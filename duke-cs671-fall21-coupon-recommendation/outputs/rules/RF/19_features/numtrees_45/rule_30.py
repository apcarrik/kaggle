def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Temperature, obj[3]: Time, obj[4]: Coupon, obj[5]: Coupon_validity, obj[6]: Gender, obj[7]: Age, obj[8]: Maritalstatus, obj[9]: Children, obj[10]: Education, obj[11]: Occupation, obj[12]: Income, obj[13]: Bar, obj[14]: Coffeehouse, obj[15]: Restaurantlessthan20, obj[16]: Restaurant20to50, obj[17]: Direction_same, obj[18]: Distance
	# {"feature": "Restaurantlessthan20", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[15]<=2.0:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[11]>1:
			return 'True'
		elif obj[11]<=1:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[15]>2.0:
		# {"feature": "Coupon_validity", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[5]>0:
			# {"feature": "Gender", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[6]>0:
				return 'False'
			elif obj[6]<=0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					return 'False'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
