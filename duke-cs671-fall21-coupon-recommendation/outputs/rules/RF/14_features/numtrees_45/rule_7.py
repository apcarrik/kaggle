def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[7]<=20:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]>2:
					# {"feature": "Income", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[8]>0:
						return 'True'
					elif obj[8]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[6]>2:
				return 'True'
			else: return 'True'
		elif obj[10]<=0.0:
			# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[2]<=3:
				return 'False'
			elif obj[2]>3:
				# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=0:
					return 'False'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[7]>20:
		return 'False'
	else: return 'False'
