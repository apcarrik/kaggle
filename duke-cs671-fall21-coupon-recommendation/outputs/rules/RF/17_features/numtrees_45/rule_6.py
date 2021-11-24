def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Income", "instances": 16, "metric_value": 0.3373, "depth": 2}
		if obj[11]<=6:
			return 'True'
		elif obj[11]>6:
			return 'False'
		else: return 'False'
	elif obj[3]>3:
		# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 2}
		if obj[6]>3:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[9]<=0:
				return 'True'
			elif obj[9]>0:
				return 'False'
			else: return 'False'
		elif obj[6]<=3:
			return 'False'
		else: return 'False'
	else: return 'False'
