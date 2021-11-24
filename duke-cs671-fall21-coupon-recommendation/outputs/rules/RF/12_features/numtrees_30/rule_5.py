def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Bar", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[7]<=0.0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[6]<=6:
				# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[9]>0.0:
					return 'False'
				elif obj[9]<=0.0:
					return 'True'
				else: return 'True'
			elif obj[6]>6:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[7]>0.0:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Age", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[4]>0:
			return 'True'
		elif obj[4]<=0:
			# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[8]<=2.0:
				return 'True'
			elif obj[8]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
