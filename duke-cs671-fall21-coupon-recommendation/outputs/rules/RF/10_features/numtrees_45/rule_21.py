def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[7]>0.0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[2]>1:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[4]>4:
				return 'True'
			elif obj[4]<=4:
				# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[5]<=0.0:
					return 'False'
				elif obj[5]>0.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[5]<=3.0:
					return 'True'
				elif obj[5]>3.0:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[7]<=0.0:
		# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[5]<=2.0:
			return 'False'
		elif obj[5]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
