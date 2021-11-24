def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[9]<=2.0:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[7]>4:
			# {"feature": "Age", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[4]>0:
				# {"feature": "Bar", "instances": 16, "metric_value": 0.3373, "depth": 4}
				if obj[8]<=2.0:
					return 'True'
				elif obj[8]>2.0:
					return 'False'
				else: return 'False'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		elif obj[7]<=4:
			# {"feature": "Age", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[4]<=2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0:
					return 'True'
				elif obj[6]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[9]>2.0:
		# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[6]<=2:
			return 'False'
		elif obj[6]>2:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
