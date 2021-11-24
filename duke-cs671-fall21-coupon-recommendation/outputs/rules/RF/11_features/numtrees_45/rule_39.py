def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]>4:
		# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]<=2:
			return 'False'
		elif obj[0]>2:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]>2:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>0:
					return 'False'
				elif obj[3]<=0:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[5]<=4:
		# {"feature": "Bar", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[6]<=2.0:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[10]<=2:
				return 'True'
			elif obj[10]>2:
				# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=0:
					return 'True'
				elif obj[3]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[6]>2.0:
			return 'False'
		else: return 'False'
	else: return 'True'
