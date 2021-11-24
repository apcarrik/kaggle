def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[4]<=1:
		# {"feature": "Time", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[4]>1:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]>3:
				return 'False'
			elif obj[2]<=3:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[6]>0:
					return 'False'
				elif obj[6]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[10]>1.0:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	else: return 'False'
