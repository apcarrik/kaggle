def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]>2:
		# {"feature": "Bar", "instances": 13, "metric_value": 0.8905, "depth": 2}
		if obj[7]<=1.0:
			# {"feature": "Direction_same", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[10]<=0:
				return 'True'
			elif obj[10]>0:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=0:
					return 'True'
				elif obj[0]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]>1.0:
			return 'False'
		else: return 'False'
	elif obj[4]<=2:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[6]<=17:
			# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[8]<=3.0:
				return 'False'
			elif obj[8]>3.0:
				# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>17:
			return 'True'
		else: return 'True'
	else: return 'False'
