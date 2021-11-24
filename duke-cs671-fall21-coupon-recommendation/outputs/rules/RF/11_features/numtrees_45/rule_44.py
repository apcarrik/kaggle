def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[5]<=9:
		# {"feature": "Time", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[4]<=2:
					return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>2:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[5]>9:
		# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[7]<=2.0:
			return 'False'
		elif obj[7]>2.0:
			return 'True'
		else: return 'True'
	else: return 'False'
