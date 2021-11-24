def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[6]>1:
		# {"feature": "Coupon", "instances": 12, "metric_value": 1.0, "depth": 2}
		if obj[2]>0:
			# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[4]>0:
					return 'True'
				elif obj[4]<=0:
					return 'False'
				else: return 'False'
			elif obj[9]>1.0:
				return 'False'
			else: return 'False'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[6]<=1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[7]<=10:
			return 'True'
		elif obj[7]>10:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=1:
				return 'True'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
