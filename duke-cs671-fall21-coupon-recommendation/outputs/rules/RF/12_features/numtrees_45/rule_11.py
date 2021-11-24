def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=0:
		# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[8]<=1.0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[6]<=5:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			elif obj[6]>5:
				return 'False'
			else: return 'False'
		elif obj[8]>1.0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[5]<=2:
				return 'True'
			elif obj[5]>2:
				# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]<=3:
					return 'False'
				elif obj[4]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[10]>0:
		# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[9]>1.0:
			return 'False'
		elif obj[9]<=1.0:
			# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[4]>1:
				return 'True'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
