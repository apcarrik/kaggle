def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=3:
		# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[11]>0.0:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[7]<=2:
				return 'True'
			elif obj[7]>2:
				# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[8]>7:
					return 'True'
				elif obj[8]<=7:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[11]<=0.0:
			return 'False'
		else: return 'False'
	elif obj[2]>3:
		# {"feature": "Time", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[1]>1:
			# {"feature": "Gender", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=14:
					return 'True'
				elif obj[8]>14:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
