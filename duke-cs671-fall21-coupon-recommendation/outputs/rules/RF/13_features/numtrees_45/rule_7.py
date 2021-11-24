def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Age", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[4]<=4:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[10]<=1.0:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9183, "depth": 3}
			if obj[8]<=1.0:
				# {"feature": "Children", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[5]>0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]<=2:
						return 'False'
					elif obj[0]>2:
						return 'True'
					else: return 'True'
				elif obj[5]<=0:
					# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[9]>0.0:
						return 'True'
					elif obj[9]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>1.0:
				return 'False'
			else: return 'False'
		elif obj[10]>1.0:
			# {"feature": "Bar", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[8]<=3.0:
				return 'True'
			elif obj[8]>3.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>4:
		return 'False'
	else: return 'False'
