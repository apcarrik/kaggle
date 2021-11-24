def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Time", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[2]<=1:
			return 'False'
		elif obj[2]>1:
			# {"feature": "Age", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Weather", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[6]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>1:
		# {"feature": "Maritalstatus", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[7]>0:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[10]<=12:
				return 'False'
			elif obj[10]>12:
				return 'True'
			else: return 'True'
		elif obj[7]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
