def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[9]>1:
		# {"feature": "Bar", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[12]<=1.0:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[3]>0:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[10]>1:
					return 'True'
				elif obj[10]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		elif obj[12]>1.0:
			return 'False'
		else: return 'False'
	elif obj[9]<=1:
		# {"feature": "Passanger", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
