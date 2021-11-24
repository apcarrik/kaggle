def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[10]>1.0:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[2]>0:
			# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[8]<=6:
				return 'True'
			elif obj[8]>6:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					return 'False'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=0:
			# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=0:
				return 'False'
			elif obj[5]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[10]<=1.0:
		# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[11]<=1.0:
			# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[4]>0:
				return 'False'
			elif obj[4]<=0:
				return 'True'
			else: return 'True'
		elif obj[11]>1.0:
			return 'True'
		else: return 'True'
	else: return 'False'
