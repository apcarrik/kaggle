def findDecision(obj): #obj[0]: Driving_to, obj[1]: Passanger, obj[2]: Weather, obj[3]: Temperature, obj[4]: Time, obj[5]: Coupon, obj[6]: Coupon_validity, obj[7]: Gender, obj[8]: Age, obj[9]: Maritalstatus, obj[10]: Children, obj[11]: Education, obj[12]: Occupation, obj[13]: Income, obj[14]: Bar, obj[15]: Coffeehouse, obj[16]: Carryaway, obj[17]: Restaurantlessthan20, obj[18]: Restaurant20to50, obj[19]: Direction_same, obj[20]: Distance
	# {"feature": "Age", "instances": 20, "metric_value": 0.9341, "depth": 1}
	if obj[8]>2:
		# {"feature": "Passanger", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[5]>0:
				return 'True'
			elif obj[5]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[8]<=2:
		# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[14]>0.0:
				return 'True'
			elif obj[14]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
