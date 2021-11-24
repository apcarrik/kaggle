def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[6]>1:
		# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[5]<=1:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]>1:
					return 'True'
				elif obj[2]<=1:
					# {"feature": "Age", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>2:
						return 'False'
					elif obj[4]<=2:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]>1:
				# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[7]<=2.0:
					return 'False'
				elif obj[7]>2.0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[9]>1.0:
			return 'False'
		else: return 'False'
	elif obj[6]<=1:
		return 'True'
	else: return 'True'
