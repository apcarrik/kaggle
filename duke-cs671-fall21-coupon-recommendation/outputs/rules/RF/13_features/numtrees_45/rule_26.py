def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Children", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[5]<=0:
		# {"feature": "Age", "instances": 16, "metric_value": 0.5436, "depth": 2}
		if obj[4]<=2:
			# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[8]>1.0:
				return 'True'
			elif obj[8]<=1.0:
				# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[7]>6:
					return 'True'
				elif obj[7]<=6:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[4]>2:
			return 'True'
		else: return 'True'
	elif obj[5]>0:
		# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[12]>1:
			return 'False'
		elif obj[12]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
