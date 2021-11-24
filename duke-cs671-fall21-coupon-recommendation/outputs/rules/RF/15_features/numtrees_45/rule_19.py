def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[7]>0:
			# {"feature": "Coupon_validity", "instances": 13, "metric_value": 0.9612, "depth": 3}
			if obj[3]>0:
				# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Income", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]>2:
						return 'False'
					elif obj[9]<=2:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[3]<=0:
				# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[7]<=0:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[8]>1:
				return 'True'
			elif obj[8]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
