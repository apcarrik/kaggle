def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon_validity", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[4]<=0:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.5746, "depth": 2}
		if obj[3]>1:
			return 'True'
		elif obj[3]<=1:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[9]<=2:
				return 'False'
			elif obj[9]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]>0:
		# {"feature": "Age", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[6]<=2:
			return 'False'
		elif obj[6]>2:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[3]>3:
				# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>0:
					return 'False'
				elif obj[2]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=3:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
