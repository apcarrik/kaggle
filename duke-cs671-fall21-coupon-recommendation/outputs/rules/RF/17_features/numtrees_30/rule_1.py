def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[3]>2:
		# {"feature": "Time", "instances": 22, "metric_value": 0.976, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Gender", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[6]>2:
					return 'True'
				elif obj[6]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>2:
			# {"feature": "Income", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[11]<=4:
				return 'True'
			elif obj[11]>4:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[6]>2:
					return 'False'
				elif obj[6]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=2:
		# {"feature": "Maritalstatus", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[7]>0:
			return 'True'
		elif obj[7]<=0:
			# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[12]>1.0:
				return 'True'
			elif obj[12]<=1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
