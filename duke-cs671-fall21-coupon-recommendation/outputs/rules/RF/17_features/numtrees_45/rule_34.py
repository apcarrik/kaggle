def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[6]>0:
		# {"feature": "Gender", "instances": 18, "metric_value": 0.5033, "depth": 2}
		if obj[5]<=0:
			return 'True'
		elif obj[5]>0:
			# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]>0:
					return 'False'
				elif obj[8]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[6]<=0:
		# {"feature": "Time", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[2]<=1:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
